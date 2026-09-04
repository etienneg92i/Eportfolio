#!/usr/bin/env python3
"""PreToolUse (Bash) enforcement : refuse `git commit` quand le site est cassé.

C'est le plancher sous le skill `verify-page-render`. Le skill demande au modèle
de contrôler le rendu ; ce hook le garantit même quand le modèle ne le fait pas.

Pourquoi ne pas simplement demander : le modèle vérifie 9 fois sur 10. La 10e
commite un `content.py` qui n'importe pas ou un gabarit cassé, et le prochain
déploiement montre une 500 ou une page défigurée à un recruteur — le seul
résultat que ce dépôt ne peut pas encaisser. La 10e existe par non-déterminisme
(même prompt, même contexte, sortie différente), pas par négligence : « ça n'est
jamais arrivé » est un échantillon, pas une garantie. Un blocage est un plancher.

Bloque (exit 2) un `git commit` si :
  - `python -c "import content"` échoue, ou
  - le script de rendu autonome sort en erreur (gabarit cassé, séparateurs
    orphelins, nombre de cartes incohérent, délimiteurs Jinja résiduels).

Toute commande qui n'est pas un `git commit` passe sans contrôle.
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)

cmd = (data.get("tool_input") or {}).get("command", "")
if not isinstance(cmd, str) or not cmd.strip():
    sys.exit(0)


def sanitise(text):
    text = re.sub(r"<<-?\s*(['\"]?)(\w+)\1.*?\n\2\b", " ", text, flags=re.S)
    text = re.sub(r"<<-?\s*(['\"]?)\w+\1.*", " ", text, flags=re.S)
    text = re.sub(r'"[^"]*"', '""', text)
    text = re.sub(r"'[^']*'", "''", text)
    return text


scan = sanitise(cmd)
if not re.search(r"\bgit\s+commit\b", scan):
    sys.exit(0)

proj = Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path.cwd())


def block(detail):
    sys.stderr.write(
        "BLOCKED : refus de commiter, le site est cassé.\n"
        f"{detail}\n"
        "Corrige, relance le skill verify-page-render, puis recommite.\n"
    )
    sys.exit(2)


r = subprocess.run(
    [sys.executable, "-c", "import content"],
    cwd=proj, capture_output=True, text=True,
)
if r.returncode != 0:
    block("  `import content` échoue :\n" + (r.stderr.strip() or r.stdout.strip()))

script = proj / ".claude" / "skills" / "verify-page-render" / "scripts" / "render.py"
if script.exists():
    r = subprocess.run(
        [sys.executable, str(script)],
        cwd=proj, capture_output=True, text=True,
    )
    if r.returncode != 0:
        block("  le rendu de index.html échoue :\n" + (r.stdout.strip() or r.stderr.strip()))

sys.exit(0)
