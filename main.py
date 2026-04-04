from pathlib import Path

from fastapi import Depends, FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlmodel import Field, Session, SQLModel, create_engine, select

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="Mon ePortfolio", version="1.0")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


class Project(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    titre: str
    description: str


sqlite_file_name = BASE_DIR / "portfolio.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


def seed_projects():
    with Session(engine) as session:
        if session.exec(select(Project)).first():
            return
        session.add_all(
            [
                Project(titre="Portfolio web", description="Mon site ePortfolio."),
                Project(
                    titre="Projet RenovTaCana", description="En cours de developpement."
                ),
            ]
        )
        session.commit()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    seed_projects()


profil = {
    "nom": "Etienne Girard",
    "titre": "Etudiant en Data / IA",
    "presentation": "Bienvenue sur mon ePortfolio.",
}
competences = ["Python", "SQL", "FastAPI", "HTML", "CSS"]


@app.get("/", response_class=HTMLResponse)
def accueil(request: Request, session: Session = Depends(get_session)):
    projets = session.exec(select(Project)).all()
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "profil": profil,
            "competences": competences,
            "projets": projets,
        },
    )


@app.post("/projets")
def ajouter_projet(
    titre: str = Form(...),
    description: str = Form(...),
    session: Session = Depends(get_session),
):
    session.add(Project(titre=titre, description=description))
    session.commit()
    return RedirectResponse(url="/", status_code=303)


@app.post("/projets/{projet_id}/supprimer")
def supprimer_projet(projet_id: int, session: Session = Depends(get_session)):
    projet = session.get(Project, projet_id)
    if projet:
        session.delete(projet)
        session.commit()
    return RedirectResponse(url="/", status_code=303)
