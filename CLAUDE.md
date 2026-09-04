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

### Vérifier le rendu

Après un changement de `content.py` ou `templates/index.html`, suivre le skill
`verify-page-render` avant de commiter. Il se déclenche seul via sa description.

Garde-fou : un `git commit` est **bloqué** si `content.py` n'importe pas ou si
`index.html` ne rend pas (`.claude/hooks/block-broken-commit.py`, côté agent).
Même contrôle côté git : `git config core.hooksPath .githooks` (une fois par
clone) active `.githooks/pre-commit`.

### Issue tracker

Issues and specs live in GitHub Issues for `etienneg92i/Projet-eportfolio`, via the `gh` CLI. See `docs/agents/issue-tracker.md`.

`gh` n'est pas dans le PATH des shells outils : l'appeler par son chemin complet, `C:\Program Files\GitHub CLI\gh.exe`.

### Triage labels

Default canonical vocabulary — `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: one `CONTEXT.md` + `docs/adr/` at the repo root. See `docs/agents/domain.md`.
