import hashlib
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
        },
    )
