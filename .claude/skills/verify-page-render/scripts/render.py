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
    competences=content.competences,
    langues=content.langues,
    interets=content.interets,
    projets=content.projets,
    experiences=content.experiences,
    formations=content.formations,
    css_version=1,
)

try:
    html = env.get_template("index.html").render(**ctx)
except Exception as exc:  # StrictUndefined, syntaxe Jinja, etc.
    print(f"ECHEC RENDU : {type(exc).__name__}: {exc}")
    sys.exit(1)

out = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO / "_render.html"
out.write_text(html, encoding="utf-8")
print(f"rendu -> {out}  ({len(html)} octets)")


def slice_section(sid, nextid):
    i = html.find(f'id="{sid}"')
    j = html.find(f'id="{nextid}"') if nextid else len(html)
    return html[i:j] if i != -1 else ""


problems = []

if "{{" in html or "}}" in html:
    problems.append("délimiteurs Jinja ({{ ou }}) dans la sortie")
for bad in ("Undefined", "<strong></strong>", "<strong> </strong>"):
    if bad in html:
        problems.append(f"présence de {bad!r}")

for m in re.finditer(r'<p class="meta">(.*?)</p>', html, re.S):
    seg = " ".join(m.group(1).split())
    if not seg:
        problems.append("ligne <p class=\"meta\"> vide")
    elif seg.startswith("·") or seg.endswith("·") or "· ·" in seg:
        problems.append(f"séparateur ' · ' orphelin : {seg!r}")

card_counts = {
    "projets": (len(content.projets), html.count("project-card")),
    "experiences": (
        len(content.experiences),
        slice_section("experiences", "formations").count('<article class="card">'),
    ),
    "formations": (
        len(content.formations),
        slice_section("formations", "projets").count('<article class="card">'),
    ),
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
