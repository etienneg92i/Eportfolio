"""Rend templates/index.html sans FastAPI/uvicorn.

Usage : python .claude/skills/verify-page-render/scripts/render.py [sortie.html]

Écrit le HTML rendu (par défaut `_render.html` à la racine) et imprime des
contrôles automatiques. Sort en code 1 si un contrôle échoue.
"""
import re
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined

REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO))
import content  # noqa: E402

env = Environment(
    loader=FileSystemLoader(str(REPO / "templates")),
    undefined=StrictUndefined,  # casse sur une faute de frappe au lieu de rendre vide
)
env.globals["url_for"] = lambda *a, **k: "#"

ctx = dict(
    profil=content.profil,
    faits=content.faits,
    competences=content.competences,
    langues=content.langues,
    interets=content.interets,
    projets=content.projets,
    experiences=content.experiences,
    formations=content.formations,
    css_version=1,
    person_jsonld="",  # calcule dans main.py ; vide suffit pour le rendu
)

try:
    html = env.get_template("index.html").render(**ctx)
except Exception as exc:  # StrictUndefined, syntaxe Jinja, etc.
    print(f"ECHEC RENDU : {type(exc).__name__}: {exc}")
    sys.exit(1)

out = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO / "_render.html"
out.write_text(html, encoding="utf-8")
print(f"rendu -> {out}  ({len(html)} octets)")

# La page 404 partage header/footer et le systeme visuel : elle doit rendre.
try:
    html_404 = env.get_template("404.html").render(
        profil=content.profil, css_version=1
    )
    if "{{" in html_404 or "}}" in html_404 or "Undefined" in html_404:
        print("ECHEC RENDU 404.html : delimiteur Jinja ou Undefined dans la sortie")
        sys.exit(1)
    print(f"rendu 404.html OK  ({len(html_404)} octets)")
except Exception as exc:
    print(f"ECHEC RENDU 404.html : {type(exc).__name__}: {exc}")
    sys.exit(1)


def between(start, end):
    """Tranche de `html` entre le premier `start` et le `end` suivant."""
    i = html.find(start)
    if i == -1:
        return ""
    j = html.find(end, i + len(start)) if end else -1
    return html[i:j] if j != -1 else html[i:]


problems = []

if "{{" in html or "}}" in html:
    problems.append("délimiteurs Jinja ({{ ou }}) dans la sortie")
for bad in ("Undefined", "<strong></strong>", "<strong> </strong>"):
    if bad in html:
        problems.append(f"présence de {bad!r}")

# Les cinq vues doivent être rendues.
for view in ("accueil", "apropos", "parcours", "experience", "contact"):
    if f'data-view="{view}"' not in html:
        problems.append(f"vue absente : data-view=\"{view}\"")

# Ligne meta concaténée des projets : pas de séparateur ' · ' orphelin.
for m in re.finditer(r'<p class="project__meta">(.*?)</p>', html, re.S):
    seg = " ".join(m.group(1).split())
    if not seg:
        problems.append('ligne <p class="project__meta"> vide')
    elif seg.startswith("·") or seg.endswith("·") or "· ·" in seg:
        problems.append(f"séparateur ' · ' orphelin : {seg!r}")

# Nombre de cartes rendues == nombre d'entrées dans content.py.
# Vue "parcours" : Formations puis Projets. Vue "experience" : Expériences.
parcours_html = between('id="parcours"', 'id="experience"')
exp_html = between('id="experience"', 'id="contact"')
form_html = parcours_html.split(">Projets<")[0]
projets_html = parcours_html.split(">Projets<")[1] if ">Projets<" in parcours_html else ""

card_counts = {
    "projets": (len(content.projets), projets_html.count('<article class="project">')),
    "experiences": (len(content.experiences), exp_html.count('<article class="entry">')),
    "formations": (len(content.formations), form_html.count('<article class="entry">')),
}
for name, (want, got) in card_counts.items():
    mark = "ok" if want == got else "MISMATCH"
    print(f"  {name:12} data={want}  rendu={got}  [{mark}]")
    if want != got:
        problems.append(f"{name}: {want} entrées mais {got} cartes rendues")

if problems:
    print("\nPROBLEMES :")
    for p in problems:
        print(f"  - {p}")
    sys.exit(1)

print("\ncontrôles automatiques OK — relis quand même à l'œil les sections touchées")
