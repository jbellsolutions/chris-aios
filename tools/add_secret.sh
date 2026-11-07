#!/usr/bin/env bash
# Usage: tools/add_secret.sh NAME
# Reads a secret without echoing it and stores NAME=value in .env.local (git-ignored).
set -euo pipefail
name="${1:?usage: tools/add_secret.sh NAME}"
[[ "$name" =~ ^[A-Z][A-Z0-9_]*$ ]] || { echo "NAME must be UPPER_SNAKE_CASE" >&2; exit 1; }
cd "$(dirname "$0")/.."
read -r -s -p "Paste $name (input hidden): " value; echo
[ -n "$value" ] || { echo "empty; nothing saved" >&2; exit 1; }
touch .env.local; chmod 600 .env.local
grep -v "^${name}=" .env.local > .env.local.tmp || true
printf '%s=%s\n' "$name" "$value" >> .env.local.tmp
mv .env.local.tmp .env.local; chmod 600 .env.local
echo "Saved $name to .env.local"
