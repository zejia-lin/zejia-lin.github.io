---
title: "Table"
description: ""
lead: ""
date: 2023-01-12T18:34:30+08:00
lastmod: 2023-01-12T18:34:30+08:00
draft: false
images: []
menu:
  wiki:
    parent: "latex"
weight: 999
toc: true
---

# Misc

愚蠢的tlmgr要远程版本低于本地咋办，把年份换成本地的

```bash
sudo tlmgr option repository https://mirrors.tuna.tsinghua.edu.cn/tex-historic-archive/systems/texlive/2022/tlnet-final
```


# Long Table

```
\begin{center}
    \begin{longtable}[!htbp]{c|c|ccc|c|c|ccc}
      \caption{迭代次数和误差} \vspace*{-1em} 
      \label{tab:exp-result} \\
      
      \toprule 
      函数 & 初值 & 方法 & \makecell[c]{迭代\\次数} & \makecell[c]{与$x^*$\\误差} & 函数 & 初值 & 方法 & \makecell[c]{迭代\\次数} & \makecell[c]{与$x^*$\\误差} \\ 
      \midrule 
      \endfirsthead
      
      \multicolumn{10}{c}{{\tablename\ \thetable{} 迭代次数和误差（接上页）}} \\
      \toprule 
      函数 & 初值 & 方法 & \makecell[c]{迭代\\次数} & \makecell[c]{与$x^*$\\误差} & 函数 & 初值 & 方法 & \makecell[c]{迭代\\次数} & \makecell[c]{与$x^*$\\误差} \\ 
      \midrule 
      \endhead
      
      \bottomrule 
      \multicolumn{10}{r}{{续下页}} \\
      \endfoot
      
      \bottomrule
      \endlastfoot
    \end{longtable}
\end{center}
```

# Minted Code

abcdefg
