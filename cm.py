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

import os
import re
import sys
import shutil
import shlex
import argparse
import subprocess


if __name__ == '__main__':
    basedir = os.path.dirname(os.path.abspath(__file__))
    parser = argparse.ArgumentParser()
    parser.add_argument("msg")
    args = parser.parse_args()
    msg = args.msg
    print('In ./content/en/shared')
    subprocess.check_call(['git', 'add', '.'], cwd='content/en/shared')
    subprocess.call(['git', 'commit', '-m', f'{msg}'], cwd='content/en/shared')
    subprocess.check_call(['git', 'push'])
    print('In ./')
    subprocess.check_call(['git', 'add', '.'], cwd=basedir)
    subprocess.call(['git', 'commit', '-m', f'{msg}'], cwd=basedir)
