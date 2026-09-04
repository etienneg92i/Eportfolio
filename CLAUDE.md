# CLAUDE.md

Guidance for agents working in this repository.

## Le projet

ePortfolio statique : FastAPI + Jinja2, une seule page (`templates/index.html`).
Pas de base de données, pas d'authentification.

- **Contenu du site** : `content.py` (profil, compétences, projets, expériences,
  formations). C'est la source unique de vérité — éditer ce fichier puis commiter.
- **Lancer en local** : `conda activate data_manipulation` puis `uvicorn main:app --reload`
- **Dépendances** : `requirements.txt` (fastapi, uvicorn, jinja2)

## Vérifier un changement de contenu ou de template

Avant de commiter une modif de `content.py` ou `templates/index.html`, regarder
le HTML rendu de la section touchée — pas seulement le diff. Juger au cas par
cas ce qu'il faut regarder : une coquille dans un texte se relit à l'œil, un
champ optionnel ajouté/retiré demande de vérifier le rendu quand il est absent
(séparateurs ` · ` orphelins, blocs vides).

Méthode selon l'environnement : si `conda activate data_manipulation` est
disponible, `uvicorn main:app --reload`. Sinon, rendre le template seul sans
serveur — `jinja2` + les données de `content.py`, `url_for` stubbé.

## Agent skills

### Issue tracker

Issues and specs live in GitHub Issues for `etienneg92i/Projet-eportfolio`, via the `gh` CLI. See `docs/agents/issue-tracker.md`.

`gh` n'est pas dans le PATH des shells outils : l'appeler par son chemin complet, `C:\Program Files\GitHub CLI\gh.exe`.

### Triage labels

Default canonical vocabulary — `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: one `CONTEXT.md` + `docs/adr/` at the repo root. See `docs/agents/domain.md`.
