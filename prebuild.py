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


shared_index_fron_matter = """---
title: "Shared Files"
description: ""
date: 2023-05-03T21:49:48+08:00
lastmod: 2023-05-03T21:49:48+08:00
draft: true
images: []
---


"""



def remove_front_matter(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        content = re.sub(r'^---[\s\S]*?---\n', '', content)
        content = '# Zejia LIN (林泽佳)\n' + content
    with open(file_path, 'w') as file:
        file.write(content)


def make_shared_file_index(dirname):
    filenames = sorted(os.listdir(dirname))
    filenames.remove('index.md')
    with open(os.path.join(dirname, 'index.md'), 'w') as index_md:
        index_md.write(shared_index_fron_matter)
        index_md.write('<ul align=\"left\">\n')
        for filename in filenames:
            oldname = filename
            filename = filename.replace(' ', '-')
            os.rename(os.path.join(dirname, oldname), os.path.join(dirname, filename))
            index_md.write(f'  <li><a href="{filename}">{filename}</a></li>\n') 
        index_md.write('<ul>\n\n<br><br><br>\n')


if __name__ == '__main__':
    basedir = os.path.dirname(os.path.abspath(__file__))
    content_dir = os.path.join(basedir, 'content', 'en')
    index_path = os.path.join(content_dir, '_index.md')
    shared_dir = os.path.join(content_dir, 'shared')
    readme_path = os.path.join(basedir, 'README.md')
    shutil.copy2(index_path, readme_path)
    remove_front_matter(readme_path)
    make_shared_file_index(shared_dir)
    
