# CLAUDE.md

Guidance for agents working in this repository.

## Le projet

ePortfolio statique : FastAPI + Jinja2, une seule page (`templates/index.html`).
Pas de base de données, pas d'authentification.

- **Contenu du site** : `content.py` (profil, compétences, projets, expériences,
  formations). C'est la source unique de vérité — éditer ce fichier puis commiter.
- **Lancer en local** : `conda activate data_manipulation` puis `uvicorn main:app --reload`
- **Dépendances** : `requirements.txt` (fastapi, uvicorn, jinja2)

## Agent skills

### Issue tracker

Issues and specs live in GitHub Issues for `etienneg92i/Projet-eportfolio`, via the `gh` CLI. See `docs/agents/issue-tracker.md`.

### Triage labels

Default canonical vocabulary — `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: one `CONTEXT.md` + `docs/adr/` at the repo root. See `docs/agents/domain.md`.
