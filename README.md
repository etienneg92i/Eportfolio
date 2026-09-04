# ePortfolio — Étienne Girard

Portfolio personnel : un site statique d'une seule page qui présente profil,
compétences, parcours et projets.

## Stack

- **FastAPI** + **Jinja2** — une route (`GET /`), un template (`templates/index.html`)
- Pas de base de données, pas d'authentification
- CSS maison (`static/style.css`)

## Lancer en local

```bash
conda activate data_manipulation      # ou : pip install -r requirements.txt
uvicorn main:app --reload
```

Puis ouvrir http://127.0.0.1:8000

## Modifier le contenu

Tout le contenu vit dans `content.py` (profil, compétences, projets,
expériences, formations) — source unique de vérité. Éditer ce fichier puis
commiter.

## Contribuer

Conventions, glossaire du domaine et outillage agent : `CLAUDE.md`, `CONTEXT.md`,
`docs/`.
