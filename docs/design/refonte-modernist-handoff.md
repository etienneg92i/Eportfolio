# Handoff : refonte ePortfolio — Modernist

> Spec de design d'origine, conservée comme référence pour reproduire les vues
> au pixel. La décision et ses conséquences sont dans
> [`docs/adr/0001-systeme-visuel-modernist.md`](../adr/0001-systeme-visuel-modernist.md).
> Les fichiers `design/*.dc.html` mentionnés ci-dessous étaient des prototypes de
> l'outil de design ; ils n'ont pas été versionnés.

## Overview

Refonte visuelle du site `etienneg92i/Eportfolio` (ePortfolio d'Étienne Girard).
Le site actuel est mono-page : une route `GET /`, un template `templates/index.html`, un CSS
maison `static/style.css`, contenu dans `content.py`.

La refonte passe la même information en **cinq vues** — Accueil, À propos, Projets, Parcours,
Contact — sur un système visuel « Modernist » : grille modulaire visible, filets 2px, aucun
arrondi, un seul accent rouge, tout en Archivo, alignement systématiquement flush left.

Le contenu est **identique à `content.py`** : aucun texte n'a été réécrit. Les seules
différences de rendu sont des regroupements (métadonnées concaténées en une ligne) et la
suppression des `&amp;` échappés (voir « Points d'attention »).

## About the Design Files

Les fichiers de `design/` sont des **références de design en HTML** — des prototypes qui
montrent le rendu et le comportement attendus, pas du code de production à copier tel quel.

La tâche est de **recréer ces designs dans l'environnement du dépôt** : FastAPI + Jinja2 +
CSS maison. Concrètement : réécrire `templates/index.html` (ou le découper en templates par
vue) et remplacer `static/style.css`, en gardant `content.py` comme unique source de vérité.
Ne pas introduire de framework front : le projet est un site statique servi par Jinja2, et
tout le design se fait en HTML + CSS.

Les fichiers `.dc.html` s'ouvrent dans un navigateur pour référence. Leur structure interne
(balises `<x-dc>`, `<sc-for>`, `support.js`) est un artefact de l'outil de design :
`<sc-for list="..." as="x">` correspond exactement à `{% for x in ... %}` en Jinja2, et
`<sc-if value="...">` à un `{% if %}` / à la vue active.

## Fidelity

**High-fidelity.** Couleurs, typographie, espacements et filets sont définitifs — les valeurs
exactes sont dans « Design Tokens » et reprises inline dans le HTML de référence. À recréer
au pixel.

## Écran par écran

Toutes les vues partagent :

- **Fond** `#f3f2f2`, texte `#201e1d`, police Archivo partout.
- **Conteneur** `max-width: 1180px; margin-inline: auto; padding: 0 32px`.
- **Header collant** : `position: sticky; top: 0; background: #f3f2f2; border-bottom: 2px solid #201e1d; z-index: 20`,
  hauteur mini 72px, contenu en `display:flex; justify-content:space-between; align-items:stretch; gap:32px`.
  - À gauche, deux lignes empilées, centrées verticalement : « ETIENNE GIRARD » (Archivo 800,
    17px, `letter-spacing:-.01em`, uppercase) et « DATA & IA » (12px, `letter-spacing:.14em`,
    uppercase, `#605d5d`).
  - À droite, la nav : boutons `<button>` remis à zéro (fond transparent, pas de bordure),
    13px, `letter-spacing:.12em`, uppercase, `padding: 0 18px`, `border-bottom: 3px solid transparent`.
    Onglet actif : `font-weight:700`, couleur `#201e1d`, `border-bottom-color:#ec3013`.
    Onglet inactif : `font-weight:500`, couleur `#605d5d`.
  - Onglets, dans cet ordre : Accueil, À propos, Projets, Parcours, Contact.
- **Footer** : `border-top: 2px solid #201e1d`, `padding: 24px 32px`, flex avec
  `justify-content:space-between`, 13px, `#605d5d`. À gauche « © 2026 Etienne Girard », à
  droite deux liens (E-mail → `mailto:etienne.p.girard@gmail.com`, GitHub →
  `https://github.com/etienneg92i`, `target="_blank" rel="noopener"`) séparés par `gap:20px`.
- Chaque changement de vue remet le scroll en haut (`window.scrollTo(0,0)`).

### 1. Accueil

**But** : identité, positionnement, accès rapide aux projets et au contact.

**Hero** — section terminée par `border-bottom: 2px solid #201e1d`. Grille
`grid-template-columns: repeat(auto-fit, minmax(280px,1fr)); gap:0`.

- Cellule gauche : `padding: 64px 40px 56px 0`, `border-right: 2px solid var(--color-divider)`,
  flex colonne centrée verticalement, `gap:24px`.
  - Sur-titre « PORTFOLIO 2026 » : 12px, `letter-spacing:.16em`, uppercase, `#ae1800`.
  - H1 sur trois lignes : « Étudiant / ingénieur / Data & IA », Archivo 800,
    `font-size: clamp(40px, 6vw, 76px)`, `line-height:.98`, `letter-spacing:-.03em`, uppercase.
    La troisième ligne (« Data & IA ») est en `#ec3013`.
  - Paragraphe : 17px, `line-height:1.6`, `max-width:44ch`, `#444141`. Texte = les deux
    premières phrases de `profil.presentation`.
  - Boutons (`margin-top:8px`, `gap:12px`) : « Voir les projets » en `.btn.btn-primary`
    (aplat rouge) → vue Projets ; « Me contacter » en `.btn.btn-secondary` → vue Contact.
- Cellule droite : `padding: 64px 0 56px 40px`, `align-items:stretch`. À l'intérieur, le
  portrait remplit la cellule : conteneur `width:100%; min-height:420px; overflow:hidden;
  background:#2d2b2b`, image en `object-fit:cover; object-position:50% 30%`, filtre
  `saturate(.85) contrast(1.08) brightness(.88)` (photo en couleur, assombrie et légèrement
  désaturée — pas de noir et blanc ici).

**Bande d'infos** — section suivante, `border-bottom: 2px solid #201e1d`, grille
`repeat(5, minmax(0,1fr))` : les cinq cellules restent sur **une seule ligne**. Chaque cellule
`padding:24px` (la première sans padding gauche, la dernière sans padding droit),
séparateurs `border-right: 1px solid var(--color-divider)` sauf la dernière. Contenu :
libellé 11px `letter-spacing:.14em` uppercase `#605d5d`, valeur 15px `font-weight:700`.

| Libellé | Valeur |
| --- | --- |
| Poste | Alternant Data — Finance |
| Entreprise | Décathlon |
| École | EPF — Majeure Data & IA |
| Base | Paris, France |
| Langues | FR · EN B2 · ES B2 |

**Compétences** — section `padding: 56px 32px`, `border-bottom: 2px solid #201e1d`.
Titre de section « COMPÉTENCES » (Archivo 800, 13px, `letter-spacing:.16em`, uppercase,
`#605d5d`, `margin-bottom:32px`). Puis grille `repeat(auto-fit, minmax(260px,1fr)); gap:32px`,
un bloc par groupe de `content.py:competences` :

- `border-top: 2px solid #201e1d; padding-top:20px`.
- Titre du groupe : Archivo 800, 18px, `letter-spacing:-.01em`, `margin-bottom:16px`.
- Liste `gap:8px`, items 15px `line-height:1.5` `#444141`, `padding-left:16px`, puce
  = tiret rouge en `position:absolute; left:0; top:.6em; width:6px; height:2px; background:#ec3013`.

L'accueil s'arrête là (pas de bandeau rouge de fin — il a été retiré volontairement).

### 2. À propos

`padding: 56px 32px 80px`.

- Sur-titre « À PROPOS » (12px, `.16em`, uppercase, `#ae1800`), H1 « PROFIL »
  (`clamp(32px,5vw,56px)`, Archivo 800, `line-height:1`, `letter-spacing:-.02em`, uppercase,
  `margin-bottom:40px`).
- Paragraphe de profil complet (`profil.presentation` intégral) : 19px, `line-height:1.6`,
  `max-width:60ch`, `#444141`, `margin-bottom:56px`.
- Grille `repeat(auto-fit, minmax(280px,1fr))`, `border-top: 2px solid #201e1d`, trois
  cellules séparées par `border-right: 2px solid var(--color-divider)` (padding : `28px 40px 28px 0`,
  `28px 40px`, `28px 0 28px 40px`). Titre de cellule identique aux titres de section
  (13px, `.16em`, uppercase, `#605d5d`, `margin-bottom:20px`).
  - **Langues** : une ligne par entrée de `content.py:langues`, `display:flex;
    justify-content:space-between`, `padding:12px 0`, `border-bottom: 1px solid var(--color-divider)`.
    Langue en Archivo 800 17px, niveau en 14px `#605d5d`.
  - **Centres d'intérêt** : liste `gap:12px`, mêmes puces tiret rouge que Compétences,
    items 15px `line-height:1.55` `#444141`. Source : `content.py:interets`.
  - **Coordonnées** : trois lignes empilées (`padding:12px 0`, filet 1px sauf la dernière),
    libellé 11px `.14em` uppercase `#605d5d` + valeur 15px `font-weight:700` — Localisation
    « Paris, France », E-mail (lien `mailto:`, `word-break:break-all`), GitHub
    (lien vers `github.com/etienneg92i`).

### 3. Projets

`padding: 56px 32px 80px`. Sur-titre « RÉALISATIONS », H1 « PROJETS D'INGÉNIERIE »
(même échelle que les autres H1 de vue), sous-titre 16px `#605d5d` `max-width:52ch` :
« Une sélection de projets d'équipe, académiques et industriels. » (`margin-bottom:48px`).

Un `<article>` par projet de `content.py:projets`, empilés sans gap :
`border-top: 2px solid #201e1d; padding: 32px 0`, grille interne
`repeat(auto-fit, minmax(240px,1fr)); gap:32px`.

- Colonne gauche : titre du projet en Archivo 800 26px `line-height:1.15`
  `letter-spacing:-.02em` ; sous lui la méta en 13px `letter-spacing:.06em` uppercase
  `#605d5d` — concaténation `cadre · organisation · periode` (les champs vides sont omis,
  comme dans le template Jinja actuel).
- Colonne droite : description en 16px `line-height:1.65` `#444141` (`margin-bottom:20px`),
  puis les technos en `.tag.tag-outline`, `display:flex; flex-wrap:wrap; gap:8px`.

### 4. Parcours

`padding: 56px 32px 80px`. Sur-titre « PARCOURS », H1 sur deux lignes
« EXPÉRIENCES / & FORMATIONS » (`margin-bottom:48px`).

Deux sous-blocs, « EXPÉRIENCES » puis « FORMATIONS » (titres 13px `.16em` uppercase `#605d5d`,
`margin-bottom:20px` ; 64px de marge sous le premier bloc). Dans chacun, un `<article>` par
entrée de `content.py:experiences` / `content.py:formations` :

- `border-top: 2px solid #201e1d; padding: 24px 0`, grille
  `grid-template-columns: minmax(160px,220px) 1fr; gap:32px`.
- Colonne gauche : période en 13px `letter-spacing:.06em` uppercase `#ae1800` ; organisation
  en 15px `font-weight:700` ; lieu en 13px `#605d5d`.
- Colonne droite : intitulé en Archivo 800 20px `letter-spacing:-.01em` (`margin-bottom:8px`),
  description 15px `line-height:1.65` `#444141` `max-width:62ch`.

Les périodes affichées sont raccourcies par rapport à `content.py` (« juil. – août 2024 »
sans « · 2 mois ») ; libre au dev de garder la valeur brute si c'est plus simple.

### 5. Contact

`padding: 56px 32px 0`. Sur-titre « CONTACT », H1 sur deux lignes « TRAVAILLONS / ENSEMBLE »
(`margin-bottom:32px`), paragraphe 17px `line-height:1.65` `#444141` `max-width:48ch`
(`margin-bottom:48px`) : « En alternance Data au sein du service Finance de Décathlon.
Ouvert aux échanges pour la suite&nbsp;? Écrivez-moi. »

Bande de coordonnées : grille `repeat(auto-fit, minmax(240px,1fr))`, encadrée
`border-top: 2px solid #201e1d` et `border-bottom: 2px solid #201e1d`, trois cellules
(padding `28px 32px 28px 0`, `28px 32px`, `28px 0 28px 32px`) séparées par
`border-right: 2px solid var(--color-divider)`. Chaque cellule : libellé 12px `.14em`
uppercase `#605d5d` puis valeur/lien en Archivo 800 18px `letter-spacing:-.01em`
(E-mail avec `word-break:break-all`, GitHub `target="_blank" rel="noopener"`, Localisation
en texte simple).

**Poster de fin** — seul aplat rouge du site : `background:#ec3013; color:#fff;
margin-top:64px`, `padding: 64px 32px`. Texte en Archivo 800
`clamp(28px,4vw,48px)`, `line-height:1.05`, `letter-spacing:-.02em`, uppercase,
`max-width:24ch`, flush left : « Ouvert au réseau et aux nouvelles missions. »

## Interactions & Behavior

- **Navigation** : cinq vues exclusives. Dans le prototype c'est un state local ;
  dans le dépôt, deux implémentations valables :
  1. **Une route, cinq sections** — garder `GET /`, rendre les cinq blocs, naviguer par
     ancres (`#accueil`, `#apropos`, …) ou par un petit script de bascule. Le plus proche de
     l'existant, aucun changement dans `main.py`.
  2. **Cinq routes** — `GET /`, `/a-propos`, `/projets`, `/parcours`, `/contact`, un template
     par vue plus un `base.html` portant header et footer. Plus propre pour le SEO et le
     partage de liens ; c'est la structure que le design suppose (le titre de chaque vue est
     un H1).
  Dans les deux cas l'onglet actif doit être marqué (filet rouge 3px + `font-weight:700`).
- **États interactifs** : ils viennent du design system (`styles.css`) — survol et état
  pressé pris dans la rampe accent, focus clavier `outline: 2px solid #ec3013;
  outline-offset: 2px`. Ne pas laisser l'anneau de focus bleu par défaut, ne pas restyler
  les états localement.
- **Aucune animation**, aucune transition d'entrée : le système est flat et statique.
- **Responsive** : les grilles en `auto-fit / minmax(...)` se replient seules. Deux points à
  traiter à la main :
  - la bande d'infos de l'accueil est figée en 5 colonnes (`repeat(5, minmax(0,1fr))`) —
    prévoir un passage en 2 ou 3 colonnes sous ~900px ;
  - le hero doit passer en une colonne sous ~760px, portrait sous le texte, et les
    `border-right` devenir des `border-bottom`.

## State Management

Aucun état métier. Une seule variable : la vue courante (`"accueil" | "apropos" | "projets" |
"parcours" | "contact"`). Pas de fetch, pas de base de données, pas d'authentification —
tout le contenu vient de `content.py` au rendu du template.

## Design Tokens

Repris de `design/styles.css` (le design system Modernist). Utiliser les variables, pas les
hex en dur.

**Couleurs**

| Rôle | Valeur |
| --- | --- |
| `--color-bg` | `#f3f2f2` |
| `--color-surface` | `#eae9e9` |
| `--color-text` | `#201e1d` |
| `--color-accent` | `#ec3013` |
| `--color-divider` | `color-mix(in srgb, #201e1d 40%, transparent)` |
| Neutres | 100 `#f8f4f4` · 200 `#eae7e7` · 300 `#d7d3d3` · 400 `#bab6b6` · 500 `#9b9797` · 600 `#7d7979` · 700 `#605d5d` · 800 `#444141` · 900 `#2d2b2b` |
| Accent | 100 `#fff2ef` · 200 `#ffe0d9` · 300 `#ffc4b8` · 400 `#ff9783` · 500 `#ff563c` · 600 `#dd2b0f` · 700 `#ae1800` · 800 `#7c1405` · 900 `#4d170e` |

Usages : texte courant `--color-text`, texte secondaire `--color-neutral-700`, corps de
paragraphe `--color-neutral-800`, sur-titres et périodes `--color-accent-700` (l'accent pur
ne passe pas les 4.5:1 en taille de texte), aplats et filets d'accent `--color-accent`.

**Typographie** — `--font-heading` et `--font-body` valent tous deux
`"Archivo", system-ui, sans-serif` ; poids de titre 800. Échelle utilisée dans les vues :
11 / 12 / 13 / 14 / 15 / 16 / 17 / 18 / 19 / 20 / 26 px, H1 de vue
`clamp(32px,5vw,56px)`, H1 d'accueil `clamp(40px,6vw,76px)`, poster `clamp(28px,4vw,48px)`.

**Espacements** — `--space-1: 4px` · `--space-2: 8px` · `--space-3: 12px` ·
`--space-4: 16px` · `--space-6: 24px` · `--space-8: 32px`. Rythme vertical des vues :
56px en haut, 80px en bas, 32px de gouttière horizontale.

**Rayons** — `--radius-sm / md / lg` = **0px**. Aucun arrondi nulle part, c'est volontaire.

**Ombres** — `--shadow-sm/md/lg` existent mais ne sont **pas utilisées** : rien ne flotte,
la hiérarchie est portée par les filets (2px pour les séparations majeures, 1px à l'intérieur
d'un bloc).

## Assets

- `design/assets/portrait.jpg` — portrait fourni par Étienne. À déposer dans `static/`
  du dépôt et à référencer via `url_for('static', path='portrait.jpg')`. Traitement CSS :
  `filter: saturate(.85) contrast(1.08) brightness(.88)`, `object-fit:cover`,
  `object-position:50% 30%`.
- `design/styles.css` — feuille du design system (tokens + couche composants : `.btn`,
  `.tag`, `.card`, `.nav`, `.table`, `.hr`, `.grayscale`). Le prototype s'appuie sur
  `.btn-primary`, `.btn-secondary` et `.tag-outline`. La reprendre comme base de
  `static/style.css` plutôt que de réécrire ces composants.
- **Icônes** : aucune pour l'instant. Si besoin, le système prescrit Lucide (lucide.dev).
- **Logos Décathlon / EPF** : envisagés puis retirés, pas d'emplacement dans le design actuel.
- Archivo n'est pas embarquée dans le bundle : charger la fonte (Google Fonts ou fichiers
  locaux dans `static/`) avant de servir la page, sinon le rendu retombe sur `system-ui`.

## Points d'attention

- **`&amp;` dans `content.py`** : plusieurs chaînes contiennent des entités HTML déjà
  échappées (« Data &amp; IA », « Git &amp; GitHub », « Programmation &amp; Data »). Jinja2
  les ré-échappe, donc le site affiche littéralement « Data &amp;amp; IA ». À corriger dans
  `content.py` en écrivant simplement `&` ; le design part du principe que c'est corrigé.
- `profil.telephone` et `profil.linkedin` sont vides : le design ne les affiche pas.
  Garder les gardes `{% if %}` du template actuel si ces champs sont remplis plus tard.
- Le fichier `design/Portfolio actuel.dc.html` est la **recréation fidèle du site existant**
  (hero dégradé sombre, cartes arrondies, chips bleues). Il sert de point de comparaison
  avant/après, pas de cible.

## Files

- `design/Portfolio Modernist.dc.html` — la refonte, les cinq vues. **La cible.**
- `design/Portfolio actuel.dc.html` — recréation du site actuel, pour comparaison.
- `design/styles.css` — tokens et composants du design system Modernist.
- `design/assets/portrait.jpg` — le portrait.
- `design/support.js` — runtime de l'outil de design, nécessaire seulement pour ouvrir les
  `.dc.html` dans un navigateur. À ne pas porter dans le dépôt.

Dépôt cible : `etienneg92i/Eportfolio`, branche `main`. Fichiers concernés :
`templates/index.html`, `static/style.css`, `content.py` (correction des `&amp;`),
`main.py` (uniquement si on passe à cinq routes).
