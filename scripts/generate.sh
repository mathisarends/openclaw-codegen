#!/usr/bin/env sh
set -eu

exec python -m openclaw_codegen.generator "$@"
