# 1. Système visuel « Modernist » pour l'ePortfolio

Date : 2026-09-09

## Statut

Accepté — implémenté dans la PR #4 (`Refonte visuelle Modernist des cinq vues`).

## Contexte

Le site était mono-page : une route `GET /`, un template, un CSS maison, hero en
dégradé sombre, cartes arrondies, chips bleues. Refonte demandée pour un rendu
plus affirmé et plus lisible pour un recruteur Data/IA.

Une spec de design complète a été fournie (voir
[`docs/design/refonte-modernist-handoff.md`](../design/refonte-modernist-handoff.md)) :
grille modulaire visible, filets 2px, aucun arrondi, un seul accent rouge
(`#ec3013`), typographie Archivo partout, alignement flush left, la même
information répartie en cinq vues (Accueil, À propos, Projets, Parcours, Contact).

Deux structures possibles étaient sur la table :

1. **Une route, cinq sections** basculées côté client (ancres / petit script).
2. **Cinq routes** + un `base.html`, un template par vue.

## Décision

Système visuel Modernist, **option 1** : on garde `GET /` et un seul gabarit
`templates/index.html`. Les cinq vues sont rendues en sections et basculées côté
client par ancre (`#accueil`, `#apropos`, …), onglet actif marqué d'un filet
rouge. Sans JavaScript, les cinq sections restent empilées et les ancres
fonctionnent.

- `static/style.css` porte les tokens et composants du design system, puis le
  layout des vues. Pas de framework front, CSS pur.
- `content.py` reste la source unique de contenu ; une liste `faits` y est
  ajoutée pour la bande de l'accueil.
- Le portrait vit dans `static/`, servi via `url_for`.
- Le skill `verify-page-render` et son `render.py` sont adaptés à la nouvelle
  structure (vues `data-view`, cartes `.project` / `.entry`).

## Conséquences

**Positif**

- Aucun changement de routage ; `main.py` ne gagne qu'une variable de contexte.
- Les garde-fous de commit (`verify-page-render`, hooks) restent opérants.
- Dégradation gracieuse sans JS.

**Négatif / limites**

- Cinq `<h1>` dans le DOM (un par vue), même si une seule vue est visible — SEO
  légèrement moins net qu'avec cinq routes.
- Pas d'URL propre ni de partage direct d'une vue autrement que par `#ancre`.
- La bande d'infos de l'accueil et le hero ont un responsive traité à la main
  (breakpoints ~900px et ~760px), à maintenir si le contenu change.
- Quelques textes de mobilier (titres de vue, phrase de contact, poster) sont
  codés dans le gabarit plutôt que dans `content.py`.

Si le besoin d'URLs par vue apparaît, migrer vers l'option 2 (cinq routes +
`base.html`) reste possible sans toucher au design system.
