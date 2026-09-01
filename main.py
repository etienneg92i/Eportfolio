from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from content import (
    competences,
    experiences,
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


def get_css_version() -> int:
    """Horodatage du CSS pour forcer le rafraichissement du cache navigateur."""
    if CSS_FILE.exists():
        return CSS_FILE.stat().st_mtime_ns
    return 1


@app.get("/", response_class=HTMLResponse)
def accueil(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "profil": profil,
            "competences": competences,
            "langues": langues,
            "interets": interets,
            "projets": projets,
            "experiences": experiences,
            "formations": formations,
            "css_version": get_css_version(),
        },
    )
