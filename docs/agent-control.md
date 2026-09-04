# Agent control

**L'instruction — skill `verify-page-render`.** Il se déclenche quand l'agent
édite `content.py` ou `templates/index.html`, ou s'apprête à commiter un tel
changement : sa description nomme ces situations, et l'agent l'atteint seul sans
qu'on la lui colle. Il donne la procédure (lister les sections touchées, rendre
la page avec ou sans `uvicorn`, relire le HTML rendu de chaque section) et un
critère de fin vérifiable (texte modifié présent au mot près, pas de délimiteur
Jinja résiduel, pas de séparateur ` · ` orphelin, nombre de cartes = nombre
d'entrées, cas du champ optionnel vide rendu). Il ne se déclenche **pas** pour
un changement purement CSS (`static/style.css`) : c'est un changement visuel de
la page, donc tentant, mais il ne touche ni le contenu ni le gabarit, et son
rendu ne dépend pas des données — le skill le dit explicitement dans sa section
« Ne concerne pas ».

**L'enforcement — hook `block-broken-commit.py`.** Il bloque en dur (`exit 2`,
la commande n'est pas exécutée) tout `git commit` si `content.py` n'importe pas
ou si `index.html` ne rend pas — même contrôle côté git via
`.githooks/pre-commit`. L'instruction ne suffit pas parce que « demander » est
précisément ce que fait déjà le skill, et l'agent le suit presque toujours :
mais « presque » est une probabilité, et ces systèmes sont non déterministes —
prompt, contexte et modèle identiques, la sortie varie quand même, et ça ne
descend pas à zéro quand les modèles progressent. « Ça n'a jamais cassé la
page » est un échantillon, pas une garantie. Les neuf fois où l'agent vérifie
seul, le hook ne coûte rien ; la dixième, il est la seule chose entre une erreur
de syntaxe et une page de portfolio cassée qu'un recruteur est en train de
regarder. Un risque aussi asymétrique ne veut pas une bonne probabilité, il veut
un plancher — qui se déclenche sans la coopération du modèle.
