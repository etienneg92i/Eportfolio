from pathlib import Path
import os
import sqlite3

from fastapi import Depends, FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlmodel import Field, Session, SQLModel, create_engine, select
from starlette.middleware.sessions import SessionMiddleware

BASE_DIR = Path(__file__).resolve().parent
CSS_FILE = BASE_DIR / "static" / "style.css"
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")
SESSION_SECRET = os.getenv("SESSION_SECRET", "change-this-secret-in-prod")

app = FastAPI(title="Mon ePortfolio", version="1.0")
app.add_middleware(SessionMiddleware, secret_key=SESSION_SECRET)
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


class Project(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    titre: str
    description: str


class ExperienceProfessionnelle(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    titre: str
    description: str


class Formation(SQLModel, table=True):
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


def seed_experiences():
    with Session(engine) as session:
        if session.exec(select(ExperienceProfessionnelle)).first():
            return
        session.add_all(
            [
                ExperienceProfessionnelle(
                    titre="Stage Data Analyst",
                    description="Analyse de donnees et creation de tableaux de bord.",
                ),
            ]
        )
        session.commit()


def seed_formations():
    with Session(engine) as session:
        if session.exec(select(Formation)).first():
            return
        session.add_all(
            [
                Formation(
                    titre="Bachelor Data / IA",
                    description="Formation en data science, machine learning et Python.",
                ),
            ]
        )
        session.commit()


def migrate_legacy_schema():
    conn = sqlite3.connect(sqlite_file_name)
    try:
        cursor = conn.cursor()
        cursor.execute("PRAGMA table_info(formation)")
        rows = cursor.fetchall()
        columns = {row[1] for row in rows}

        if not rows:
            return

        if "nom" in columns:
            titre_expr = "COALESCE(NULLIF(titre, ''), nom)"
            if "titre" not in columns:
                titre_expr = "nom"

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS formation_new (
                    id INTEGER PRIMARY KEY,
                    titre VARCHAR NOT NULL,
                    description VARCHAR NOT NULL
                )
                """
            )
            cursor.execute(
                f"""
                INSERT INTO formation_new (id, titre, description)
                SELECT
                    id,
                    COALESCE({titre_expr}, 'Formation'),
                    COALESCE(description, '')
                FROM formation
                """
            )
            cursor.execute("DROP TABLE formation")
            cursor.execute("ALTER TABLE formation_new RENAME TO formation")
            conn.commit()
    finally:
        conn.close()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    migrate_legacy_schema()
    seed_projects()
    seed_experiences()
    seed_formations()


profil = {
    "nom": "Etienne Girard",
    "titre": "Etudiant en Data / IA",
    "presentation": "Bienvenue sur mon ePortfolio.",
}
competences = ["Python", "SQL", "FastAPI", "HTML", "CSS"]


def get_css_version() -> int:
    if CSS_FILE.exists():
        return CSS_FILE.stat().st_mtime_ns
    return 1


def is_admin_authenticated(request: Request) -> bool:
    return bool(request.session.get("is_admin"))


@app.get("/", response_class=HTMLResponse)
def accueil(request: Request, session: Session = Depends(get_session)):
    projets = session.exec(select(Project)).all()
    experiences = session.exec(select(ExperienceProfessionnelle)).all()
    formations = session.exec(select(Formation)).all()
    auth_error = request.query_params.get("auth") == "error"
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "profil": profil,
            "competences": competences,
            "projets": projets,
            "experiences": experiences,
            "formations": formations,
            "css_version": get_css_version(),
            "is_admin": is_admin_authenticated(request),
            "auth_error": auth_error,
        },
    )


@app.post("/login")
def login(request: Request, password: str = Form(...)):
    if password == ADMIN_PASSWORD:
        request.session["is_admin"] = True
        return RedirectResponse(url="/", status_code=303)
    request.session.pop("is_admin", None)
    return RedirectResponse(url="/?auth=error", status_code=303)


@app.post("/logout")
def logout(request: Request):
    request.session.pop("is_admin", None)
    return RedirectResponse(url="/", status_code=303)


@app.post("/projets")
def ajouter_projet(
    request: Request,
    titre: str = Form(...),
    description: str = Form(...),
    session: Session = Depends(get_session),
):
    if not is_admin_authenticated(request):
        return RedirectResponse(url="/", status_code=303)
    session.add(Project(titre=titre, description=description))
    session.commit()
    return RedirectResponse(url="/", status_code=303)


@app.post("/projets/{projet_id}/supprimer")
def supprimer_projet(
    request: Request, projet_id: int, session: Session = Depends(get_session)
):
    if not is_admin_authenticated(request):
        return RedirectResponse(url="/", status_code=303)
    projet = session.get(Project, projet_id)
    if projet:
        session.delete(projet)
        session.commit()
    return RedirectResponse(url="/", status_code=303)


@app.post("/experiences")
def ajouter_experience(
    request: Request,
    titre: str = Form(...),
    description: str = Form(...),
    session: Session = Depends(get_session),
):
    if not is_admin_authenticated(request):
        return RedirectResponse(url="/", status_code=303)
    session.add(ExperienceProfessionnelle(titre=titre, description=description))
    session.commit()
    return RedirectResponse(url="/", status_code=303)


@app.post("/experiences/{experience_id}/supprimer")
def supprimer_experience(
    request: Request, experience_id: int, session: Session = Depends(get_session)
):
    if not is_admin_authenticated(request):
        return RedirectResponse(url="/", status_code=303)
    experience = session.get(ExperienceProfessionnelle, experience_id)
    if experience:
        session.delete(experience)
        session.commit()
    return RedirectResponse(url="/", status_code=303)


@app.post("/formations")
def ajouter_formation(
    request: Request,
    titre: str = Form(...),
    description: str = Form(...),
    session: Session = Depends(get_session),
):
    if not is_admin_authenticated(request):
        return RedirectResponse(url="/", status_code=303)
    session.add(Formation(titre=titre, description=description))
    session.commit()
    return RedirectResponse(url="/", status_code=303)


@app.post("/formations/{formation_id}/supprimer")
def supprimer_formation(
    request: Request, formation_id: int, session: Session = Depends(get_session)
):
    if not is_admin_authenticated(request):
        return RedirectResponse(url="/", status_code=303)
    formation = session.get(Formation, formation_id)
    if formation:
        session.delete(formation)
        session.commit()
    return RedirectResponse(url="/", status_code=303)
