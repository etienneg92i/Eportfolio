"""Tests de rendu de la page.

Le site n'a qu'une route et un gabarit ; ces tests verifient le comportement
externe : la page repond, contient ses cinq vues, et rend chaque entree de
`content.py`. Ils completent le hook `verify-page-render` (qui, lui, ne verifie
que la forme du HTML, pas le contenu).
"""
import content
from fastapi.testclient import TestClient
from markupsafe import escape

from main import app

client = TestClient(app)


def rendu(texte: str) -> str:
    """Le texte tel qu'il apparait dans le HTML (Jinja echappe `&`, `'`, ...)."""
    return str(escape(texte))


def test_accueil_repond_200():
    r = client.get("/")
    assert r.status_code == 200
    assert "text/html" in r.headers["content-type"]


def test_les_cinq_vues_sont_presentes():
    html = client.get("/").text
    for vue in ("accueil", "apropos", "parcours", "experience", "contact"):
        assert f'data-view="{vue}"' in html


def test_pas_de_delimiteur_jinja_residuel():
    html = client.get("/").text
    assert "{{" not in html and "}}" not in html
    assert "Undefined" not in html


def test_identite_rendue():
    html = client.get("/").text
    assert rendu(content.profil["nom"]) in html
    assert rendu(content.profil["presentation"]) in html


def test_chaque_projet_est_rendu():
    html = client.get("/").text
    for projet in content.projets:
        assert rendu(projet["titre"]) in html
        assert rendu(projet["description"]) in html


def test_chaque_experience_est_rendue():
    html = client.get("/").text
    for experience in content.experiences:
        assert rendu(experience["titre"]) in html
        assert rendu(experience["description"]) in html


def test_chaque_formation_est_rendue():
    html = client.get("/").text
    for formation in content.formations:
        assert rendu(formation["titre"]) in html
        assert rendu(formation["description"]) in html


def test_chaque_competence_est_rendue():
    html = client.get("/").text
    for groupe in content.competences:
        assert rendu(groupe["categorie"]) in html
        for item in groupe["items"]:
            assert rendu(item) in html


def test_url_css_porte_l_empreinte_de_version():
    from main import CSS_VERSION

    assert f"style.css?v={CSS_VERSION}" in client.get("/").text


def test_lien_d_evitement_pointe_le_contenu():
    html = client.get("/").text
    assert '<a class="skip-link" href="#contenu">' in html
    assert 'id="contenu"' in html


def test_feuille_de_style_a_un_bloc_impression():
    css = client.get("/static/style.css").text
    assert "@media print" in css


def test_icones_et_theme_color_dans_le_head():
    html = client.get("/").text
    assert 'rel="icon"' in html and "favicon.svg" in html
    assert 'rel="apple-touch-icon"' in html
    assert '<meta name="theme-color"' in html
    assert client.get("/static/favicon.svg").status_code == 200


def test_portrait_servi_en_webp_avec_fallback():
    html = client.get("/").text
    assert "<picture>" in html
    assert "portrait.webp" in html and "portrait.jpg" in html
    r = client.get("/static/portrait.webp")
    assert r.status_code == 200
    assert len(r.content) < 100_000  # l'original faisait 733 Ko
