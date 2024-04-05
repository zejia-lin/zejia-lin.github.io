---
title: "Acm Template"
description: ""
lead: ""
date: 2024-04-05T14:53:44+08:00
lastmod: 2024-04-05T14:53:44+08:00
draft: false
images: []
menu:
  docs:
    parent: ""
    identifier: "acm-5525f9be3506fbfe3f91e18828058462"
weight: 999
toc: true
showtitle: true
---

Remove front matters in draft.

```latex
\settopmatter{printacmref=false} % Removes citation information below abstract
\renewcommand\footnotetextcopyrightpermission[1]{} % removes footnote with conference information in first column
\pagestyle{plain} % removes running headers
\settopmatter{printfolios=true}
```

Set number of authors in a row.

```latex
\settopmatter{authorsperrow=4}
```
