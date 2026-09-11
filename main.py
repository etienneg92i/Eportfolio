import hashlib
import json
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from content import (
    competences,
    experiences,
    faits,
    formations,
    interets,
    langues,
    profil,
    projets,
    traduction_en,
)

BASE_DIR = Path(__file__).resolve().parent
CSS_FILE = BASE_DIR / "static" / "style.css"
I18N_FILE = BASE_DIR / "static" / "i18n.js"

app = FastAPI(title="Mon ePortfolio", version="2.0")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


def _file_version(path: Path) -> str:
    """Empreinte du contenu d'un fichier statique, pour le cache-busting.

    Un hash du fichier, pas sa mtime : deux instances qui servent le meme
    fichier donnent la meme URL `?v=`, quel que soit l'ordre des checkouts ou
    des deploiements. Calcule une fois a l'import ; `--reload` relance le
    process quand le fichier change en dev.
    """
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()[:8]
    except OSError:
        return "dev"


CSS_VERSION = _file_version(CSS_FILE)
I18N_VERSION = _file_version(I18N_FILE)


def _hero_pitch(presentation: str) -> str:
    """Deux premieres phrases d'une presentation, pour l'accroche du hero.

    Miroir de la logique Jinja du gabarit (`{% set hero_pitch = ... %}`),
    appliquee ici a la presentation anglaise pour le bloc de traduction.
    """
    phrases = presentation.split(". ")
    pitch = ". ".join(phrases[:2])
    if len(phrases) > 2:
        pitch += "."
    return pitch


def _i18n_payload() -> str:
    """Traductions anglaises embarquees dans la page (voir static/i18n.js).

    Copie de `content.traduction_en` completee des titres composes (nom du
    profil + titre / suffixe), calcules ici pour rester synchrones avec
    `profil["nom"]`. Meme echappement que `_person_jsonld` : le bloc vit dans
    un <script type="application/json">, jamais interprete comme HTML, mais
    on echappe quand meme `<`, `>`, `&` par prudence.
    """
    data = json.loads(json.dumps(traduction_en, ensure_ascii=False))
    data["ui"]["title_accueil"] = f"{profil['nom']} — {data['profil']['titre']}"
    data["ui"]["title_404"] = f"Page not found — {profil['nom']}"
    data["profil"]["hero_pitch"] = _hero_pitch(data["profil"]["presentation"])
    # Ligne meta d'un projet (cadre · organisation · periode) : meme jointure
    # que le gabarit (`{{ meta | join(' · ') }}`), organisation non traduite
    # (nom propre), cadre/periode pris dans la traduction.
    for fr, en in zip(projets, data["projets"]):
        meta = [en.get("cadre"), fr.get("organisation"), en.get("periode")]
        en["meta"] = " · ".join(m for m in meta if m)
    raw = json.dumps(data, ensure_ascii=False, indent=2)
    return raw.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")


I18N_JSON = _i18n_payload()


def _person_jsonld() -> str:
    """Donnees structurees schema.org/Person, derivees de `content.py`.

    Rendu tel quel dans un <script type="application/ld+json"> du <head> :
    on echappe `<`, `>`, `&` en \\uXXXX pour qu'aucune valeur ne puisse
    fermer la balise ou injecter du balisage.
    """
    data = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": profil["nom"],
        "jobTitle": profil["titre"],
    }
    if profil.get("email"):
        data["email"] = f"mailto:{profil['email']}"
    sameas = [profil[k] for k in ("github", "linkedin") if profil.get(k)]
    if sameas:
        data["sameAs"] = sameas
    alumni = [
        {"@type": "EducationalOrganization", "name": f["organisation"]}
        for f in formations
        if f.get("organisation")
    ]
    if alumni:
        data["alumniOf"] = alumni
    courant = next(
        (
            e
            for e in experiences
            if e.get("organisation") and "depuis" in e.get("periode", "").lower()
        ),
        None,
    )
    if courant:
        data["worksFor"] = {"@type": "Organization", "name": courant["organisation"]}

    # `indent` : JSON-LD lisible, et surtout aucun `}}` / `{{` collé que les
    # controles anti-delimiteur-Jinja (tests, render.py) confondraient.
    raw = json.dumps(data, ensure_ascii=False, indent=2)
    return raw.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")


PERSON_JSONLD = _person_jsonld()


@app.exception_handler(404)
async def page_introuvable(request: Request, exc):
    """Page 404 maison : header/footer et systeme visuel du site, lien retour."""
    return templates.TemplateResponse(
        request,
        "404.html",
        {
            "profil": profil,
            "css_version": CSS_VERSION,
            "i18n_version": I18N_VERSION,
            "i18n_json": I18N_JSON,
        },
        status_code=404,
    )


@app.get("/", response_class=HTMLResponse)
def accueil(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "profil": profil,
            "faits": faits,
            "competences": competences,
            "langues": langues,
            "interets": interets,
            "projets": projets,
            "experiences": experiences,
            "formations": formations,
            "css_version": CSS_VERSION,
            "person_jsonld": PERSON_JSONLD,
            "i18n_version": I18N_VERSION,
            "i18n_json": I18N_JSON,
        },
    )
