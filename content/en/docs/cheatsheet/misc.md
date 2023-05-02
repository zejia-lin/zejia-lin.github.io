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

Zip and unzip

```bash
tar -czf abc.tar.gz files --exclude=pattern # gz
-cjf # bz2
tar -xzf abc.tar.gz -C path
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

