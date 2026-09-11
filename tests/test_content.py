"""Tests du garde-fou de contenu (`content._valider`).

Comportement externe attendu : un `content.py` bien forme s'importe sans bruit ;
une entree mal formee leve une `ValueError` dont le message pointe la section
fautive, de sorte que l'app refuse de demarrer plutot que de servir une page
defiguree.
"""
import content
import pytest


def test_contenu_du_repo_est_valide():
    # Ne doit rien lever : c'est le contenu reellement commite.
    content._valider()


def test_projet_sans_titre_est_rejete(monkeypatch):
    monkeypatch.setattr(content, "projets", [{"description": "sans titre"}])
    with pytest.raises(ValueError, match="projets"):
        content._valider()


def test_categorie_de_competences_sans_items_est_rejetee(monkeypatch):
    monkeypatch.setattr(content, "competences", [{"categorie": "Vide"}])
    with pytest.raises(ValueError, match="competences"):
        content._valider()


def test_champ_inconnu_est_signale(monkeypatch):
    monkeypatch.setattr(
        content, "faits", [{"libelle": "X", "valeur": "Y", "coleur": "rouge"}]
    )
    with pytest.raises(ValueError, match="coleur"):
        content._valider()


def test_profil_sans_nom_est_rejete(monkeypatch):
    bancal = dict(content.profil)
    bancal["nom"] = ""
    monkeypatch.setattr(content, "profil", bancal)
    with pytest.raises(ValueError, match="profil"):
        content._valider()


def test_technos_doit_etre_une_liste_de_chaines(monkeypatch):
    projet = dict(content.projets[0])
    projet["technos"] = "Python, R"
    monkeypatch.setattr(content, "projets", [projet])
    with pytest.raises(ValueError, match="technos"):
        content._valider()


def test_liens_bien_formes_sont_acceptes(monkeypatch):
    projet = dict(content.projets[0])
    projet["liens"] = [{"libelle": "Code source", "url": "https://github.com/x/y"}]
    monkeypatch.setattr(content, "projets", [projet])
    content._valider()  # ne doit rien lever


def test_lien_sans_url_est_rejete(monkeypatch):
    projet = dict(content.projets[0])
    projet["liens"] = [{"libelle": "Démo"}]
    monkeypatch.setattr(content, "projets", [projet])
    with pytest.raises(ValueError, match="liens"):
        content._valider()


def test_traduction_en_du_repo_est_valide():
    # Ne doit rien lever : la traduction reellement commitee est en phase
    # avec le contenu francais (memes listes, meme longueur).
    content._valider_tout()


def test_traduction_en_avec_une_entree_projet_en_moins_est_rejetee(monkeypatch):
    en = dict(content.traduction_en)
    en["projets"] = en["projets"][:1]
    monkeypatch.setattr(content, "traduction_en", en)
    with pytest.raises(ValueError, match="projets"):
        content._valider_tout()


def test_traduction_en_avec_un_libelle_ui_manquant_est_rejetee(monkeypatch):
    en = dict(content.traduction_en)
    ui = dict(en["ui"])
    del ui["nav_accueil"]
    en["ui"] = ui
    monkeypatch.setattr(content, "traduction_en", en)
    with pytest.raises(ValueError, match="ui"):
        content._valider_tout()
