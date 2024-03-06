---
title: "Run"
description: ""
lead: ""
date: 2024-03-06T14:53:31+08:00
lastmod: 2024-03-06T14:53:31+08:00
draft: false
images: []
showtitle: true
menu:
  docs:
    parent: ""
    identifier: "run-a753f71bca80045545d6da3bf3c4dfb3"
weight: 999
toc: true
---

Run benchmark scripts


```python
import subprocess
import os
import shlex
import datetime
import shutil
import tempfile


def exprange(low, hi, cnt=1):
  x = low
  step = 1. / cnt
  while x < hi:
    for i in range(cnt):
      yield int(x * (1 + step * i))
    x *= 2
  yield x

def create_temporary_copy(path):
    temp_dir = tempfile.gettempdir()
    temp_path = os.path.join(temp_dir, os.path.basename(path) + str(hash(path)))
    shutil.copy2(path, temp_path)
    return temp_path


iterations = 1
filename = 
st = datetime.datetime.now()
exe32 = create_temporary_copy()


for nsize in :
  for policy in :
    with open(filename, 'a') as fout:
      for _i in range(iterations):
        cmd = ''
        # print(cmd)
        fout.write(f'ITER {_i} ' + cmd + '\n')
        fout.flush()
        proc = subprocess.run(shlex.split(cmd),
                              stdout=fout, stderr=subprocess.STDOUT, text=True)
          

ed = datetime.datetime.now()
print(f'finish in {ed - st}')
with open(filename, 'a') as fout:
  fout.write(f'finish in {ed - st}')

```