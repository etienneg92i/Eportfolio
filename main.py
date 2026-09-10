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
)

BASE_DIR = Path(__file__).resolve().parent
CSS_FILE = BASE_DIR / "static" / "style.css"

app = FastAPI(title="Mon ePortfolio", version="2.0")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


def _css_version() -> str:
    """Empreinte du contenu CSS pour le cache-busting.

    Un hash du fichier, pas son mtime : deux instances qui servent le meme CSS
    donnent la meme URL `?v=`, quel que soit l'ordre des checkouts ou des
    deploiements. Calcule une fois a l'import ; `--reload` relance le process
    quand `style.css` change en dev.
    """
    try:
        return hashlib.sha256(CSS_FILE.read_bytes()).hexdigest()[:8]
    except OSError:
        return "dev"


CSS_VERSION = _css_version()


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
        {"profil": profil, "css_version": CSS_VERSION},
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
        },
    )
