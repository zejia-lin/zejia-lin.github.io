---
title: "Config Github"
description: ""
excerpt: ""
date: 2024-08-11T15:51:04+08:00
lastmod: 2024-08-11T15:51:04+08:00
draft: false
weight: 50
images: []
categories: []
tags: []
contributors: []
pinned: false
homepage: false
---

This page includes some snippets to manage Github ssh connection settings.

# Behind a proxy

Connect to Github with ssh behind a proxy. In the config file:

```bash
Host github.com
  Hostname ssh.github.com
  Port 443
  User git
```

Test if success.

```bash
ssh -T -p 443 git@ssh.github.com
ssh -T git@github.com
```

# Customizing name

By default `ssh-keygen -t rsa` creates the identify file named `id_rsa`. There are two options to add identify file to ssh manager.

1. In the ssh config add the `IdentifyFile` entry
2. `ssh-add --apple-use-keychain /path/to/key`

# Multiple Github profiles

To manage multiple Github ssh keys on a single machine, add a new domain in ssh config.

```bash
Host github.com-another-account
  Hostname ssh.github.com
  Port 443
  IdentityFile ~/.ssh/id_rsa_another_account
```

Test if success.

```bash
ssh -T git@github.com-another-account
```

Cloning repository.

```bash
git clone git@github.com-another-account:another_account_name/repo_name.git
```
