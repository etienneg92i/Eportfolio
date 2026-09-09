---
name: verify-page-render
description: Render index.html and check it before committing a content or template change. Use after editing content.py, after editing templates/index.html, before committing either, or when conda/uvicorn is unavailable and you still need to see the page.
---

# Vérifier le rendu de la page

Le site n'a pas de tests. La seule vérification d'un changement de contenu ou de
gabarit est de **regarder le HTML produit**, pas le diff. Ce skill donne la
procédure et un script qui rend `templates/index.html` sans FastAPI.

## Procédure

1. **Lister les vues touchées** par le diff. Les cinq vues de `index.html`
   (attribut `data-view` / `id`) : `accueil` (hero + bande d'infos + compétences),
   `apropos`, `projets`, `parcours` (expériences + formations), `contact`.

2. **Rendre la page.**
   - Si `conda activate data_manipulation` fonctionne :
     `uvicorn main:app --reload` puis ouvrir `http://127.0.0.1:8000`.
   - Sinon : `python .claude/skills/verify-page-render/scripts/render.py`
     Écrit `_render.html` à la racine et imprime les contrôles automatiques.
     (`_render.html` est ignoré par git — ne pas le commiter.)

3. **Lire le HTML rendu de chaque section touchée** et vérifier les points de la
   checklist ci-dessous.

4. **Corriger et re-rendre** jusqu'à ce que la checklist passe. Puis commiter.

## Checklist — critère de fin

Le travail est vérifié quand, pour **chaque section touchée par le diff** :

- [ ] Le texte que tu as modifié apparaît **au mot près** dans le HTML rendu.
- [ ] Aucune trace de gabarit : pas de `{{`, `}}`, ni `Undefined` dans la sortie.
- [ ] Aucun `<strong></strong>` vide ni `<p class="project__meta">` vide.
- [ ] Aucun séparateur ` · ` orphelin dans la méta projet (début/fin, ou `· ·`).
- [ ] Le nombre de cartes rendues = le nombre d'entrées dans la liste de
      `content.py` (`projets`, `experiences`, `formations`).
- [ ] La bascule de vue fonctionne : ouvrir `_render.html` ne montre qu'une vue
      à la fois une fois le JS chargé, et les cinq `data-view` sont présents.
- [ ] Si tu as ajouté ou retiré un champ **optionnel** d'un dict (un champ que
      d'autres entrées laissent vide, ex. `organisation`, `lieu`, `linkedin`),
      tu as aussi vérifié le rendu d'une entrée où ce champ est vide.

`scripts/render.py` vérifie automatiquement les points 2 à 5 (délimiteurs Jinja,
méta orpheline, nombre de cartes, présence des cinq `data-view`) et sort en
erreur s'ils échouent. Les points 1, 6 et 7 sont à ta charge, à l'œil.

## Ne concerne pas

Les changements qui ne touchent ni `content.py` ni `templates/index.html`
(CSS pur, `main.py`, docs) — pas besoin de ce skill.
