---
title : "Misc"
description: "My Wiki"
lead: ""
date: 2023-01-12T18:34:30+08:00
lastmod: 2023-01-12T18:34:30+08:00
draft: false
images: []
weight: 10
showtitle: false
main:
  abc:
    parent: "cheatsheet"
---

# Bash

A nice cheatsheet: [https://devhints.io/bash](https://devhints.io/bash)

- Zip and unzip
  ```bash
  tar -czf abc.tar.gz files --exclude=pattern # gz
  -cjf # bz2
  tar -xzf abc.tar.gz -C path
  ```
- Absolute path of current file
  ```bash
  script_dir=$(dirname $(readlink -f "$0"))
  ```
- Test if variable is set
  ```bash
  # From https://stackoverflow.com/questions/3601515/how-to-check-if-a-variable-is-set-in-bash
  if [ -z ${var+x} ]; then echo "var is unset"; else echo "var is set to '$var'"; fi
  ```
- Remove artifacts mis-installed by ninja
  ```bash
  xargs rm < install_manifest.txt
  ```


# Python

Read file line by line (using [walrus operator](https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions))

```python
with open(filename, 'r', encoding='UTF-8') as file:
    while (line := file.readline().rstrip()):
        print(line)
```

Run subprocess and get output

```python
proc = subprocess.Popen(f"commands", shell=True,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT)
stdouts, stderrs = proc.communicate()
stdouts = stdouts.decode('utf-8')
stderrs = stderrs.decode('utf-8')
```

