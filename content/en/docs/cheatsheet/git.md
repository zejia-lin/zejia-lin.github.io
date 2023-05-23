---
title: "Git"
description: ""
lead: ""
date: 2023-05-04T20:09:42+08:00
lastmod: 2023-05-04T20:09:42+08:00
draft: false
images: []
menu:
  docs:
    parent: ""
    identifier: "git-1e19364cdbbd3ba99d52cf99cf37e913"
weight: 999
toc: true
showtitle: true
---

- Checkout a specific commit to another folder
  ```bash
  git --work-tree=/path/to/folder checkout HEAD -- .
  ```
- Remove file from history
  ```bash
  git filter-branch -f --tree-filter 'rm -rf /path/to/file' HEAD
  ```

- Deinitialize submodule [[link](https://stackoverflow.com/questions/55937975/can-i-uninitialize-a-git-submodule)]
  ```bash
  git submodule deinit -f path/to/submodule
  rm -rf .git/modules/path/to/submodule
  git rm -f path/to/submodule
  git checkout -- .
  ```