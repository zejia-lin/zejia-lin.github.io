#!/bin/sh
# -*- python -*-
# This file is bilingual. The following shell code finds our preferred python.
# Following line is a shell no-op, and starts a multi-line Python comment.
# See https://stackoverflow.com/a/47886254
""":"
# prefer MY_PYTHON environment variable, python3, python
MY_PREFERRED_PYTHONS="python3 python"
for cmd in "${MY_PYTHON:-}" ${MY_PREFERRED_PYTHONS}; do
    if command -v "$cmd" >/dev/null; then
        export MY_PYTHON="$(command -v "$cmd")"
        exec "${MY_PYTHON}" "$0" "$@"
    fi
done
echo "==> Error: $0 could not find a python interpreter!" >&2
exit 1
":"""

import argparse
import sys
import os
import shlex
import subprocess

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    filename = args.filename[6:]
    if 'blog' in filename:
        filename = os.path.join(filename, 'index.md')
    subprocess.check_call(shlex.split(f"npm run create {filename}"))

