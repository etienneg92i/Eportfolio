#!/usr/bin/env python3
"""PreToolUse (Bash) guardrail: block destructive git commands.

Enforcement artifact (Lab 2). These operations have no case where the agent
should run them on its own — the answer is always "don't", so this is a hard
block, not advice. Plain `git push` is deliberately NOT blocked: this repo's
workflow is commit-and-push to main. Only history/worktree-destroying variants
are stopped.

Reads the hook JSON on stdin, exits 2 (with a stderr message Claude sees) when
the Bash command matches a dangerous pattern, exits 0 otherwise.

Matching is done on a sanitised copy of the command with heredoc bodies and
quoted strings stripped, so a commit message that merely *mentions*
`reset --hard` is not mistaken for the command itself.
"""
import json
import re
import sys

try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)

cmd = (data.get("tool_input") or {}).get("command", "")
if not isinstance(cmd, str) or not cmd.strip():
    sys.exit(0)


def sanitise(text):
    # terminated heredoc:  <<'TOK' ... \nTOK
    text = re.sub(r"<<-?\s*(['\"]?)(\w+)\1.*?\n\2\b", " ", text, flags=re.S)
    # unterminated heredoc tail
    text = re.sub(r"<<-?\s*(['\"]?)\w+\1.*", " ", text, flags=re.S)
    # blank out quoted strings (covers -m "..." / -m '...')
    text = re.sub(r'"[^"]*"', '""', text)
    text = re.sub(r"'[^']*'", "''", text)
    return text


scan = sanitise(cmd)

DANGEROUS = [
    (r"push\s+\S*\s*--force", "force-push"),
    (r"push\s+\S*\s*--mirror", "mirror-push"),
    (r"reset\s+--hard", "hard reset (discards working tree)"),
    (r"\bgit\s+clean\s+-\S*f", "git clean -f (deletes untracked files)"),
    (r"\bgit\s+clean\s+\S*\s*--force", "git clean --force"),
    (r"\bgit\s+branch\s+-D\b", "force-delete branch"),
    (r"\bgit\s+checkout\s+--(\s|$)", "git checkout -- <path> (discards changes)"),
    (r"\bgit\s+checkout\s+\.(\s|$)", "git checkout . (discards changes)"),
    (r"\bgit\s+restore\s+\.(\s|$)", "git restore . (discards changes)"),
    (r"\bgit\s+restore\s+--worktree", "git restore --worktree (discards changes)"),
    (r"\bgit\s+restore\s+--source", "git restore --source (discards changes)"),
    (r"\bgit\s+stash\s+(clear|drop)", "git stash clear/drop (destroys stashed work)"),
    (r"\bgit\s+update-ref\s+-d", "git update-ref -d (deletes a ref)"),
    (r"filter-branch", "git filter-branch (rewrites history)"),
]

for pattern, label in DANGEROUS:
    if re.search(pattern, scan):
        sys.stderr.write(
            f"BLOCKED: this command looks like {label}.\n"
            f"  command: {cmd}\n"
            f"  matched: /{pattern}/\n"
            "You do not have authority to run destructive git operations. "
            "If it is genuinely needed, ask the user to run it themselves.\n"
        )
        sys.exit(2)

sys.exit(0)
