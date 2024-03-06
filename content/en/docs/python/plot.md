---
title: "Plot"
description: "Snippets for Python matplotlib"
lead: ""
date: 2024-03-05T18:02:25+08:00
lastmod: 2024-03-05T18:02:25+08:00
draft: false
images: []
menu:
  docs:
    parent: ""
    identifier: "plot-e2c7d5486a69ba2f5a3036940e124a8a"
weight: 999
toc: true
---

## Tick

### Tick direction

```python
ax.tick_params(axis='y', which='both', direction='in')
ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
```

### Tick label format

- Scientific
  ```python
  ax.ticklabel_format(axis='x', style='sci', scilimits=(7, 7))
  ax.yaxis.get_major_formatter().set_powerlimits((0, 0))
  ```

### Tick locator

- Index locator
  ```python
  ax.xaxis.set_major_locator(plt.IndexLocator(base=1e8, offset=1.3e8))
  ```
- Log locator
  ```python
  ax.yaxis.set_major_locator(plt.LogLocator(base=10.0, numticks=10, subs=[1]))
  ax.yaxis.set_minor_locator(plt.LogLocator(base=10.0, numticks=10, subs=[_ for _ in range(10)]))
  ```


## Legend

### Combining lineplot and barplot label

```python
line_handles, labels = axes[0].get_legend_handles_labels()
bar_handles, labels = axes[1].get_legend_handles_labels()
super_legend_handles = [(line, bar[0]) for line, bar in zip(line_handles, bar_handles)]
axes.legend(super_legend_handles, labels, 
               handler_map={tuple: mpl.legend_handler.HandlerTuple(ndivide=None)},
               loc='lower left', bbox_to_anchor=(0, 1), ncol=3, handlelength=4)
```


# Useful snippets

```python
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

_liz_palette_kv = {
    "lancet": {
        "pink": "#ffc39f",
        "green": "#69c46f",
        "red": "#c91731",
        "blue": "#0b6c80",
        "black": "#000000",
        "purple": "#79459f",
        "gray": "#adb6b6"
    },
    "lancet_light": {
        "pink": "#f5e1c1",
        "green": "#8bdb92",
        "red": "#e05151",
        "blue": "#297787",
        "black": "#000000",
        "purple": "#9d6ebf",
        "gray": "#adb6b6"
    }
}


_liz_palette = {
   "lancet": np.array(["#fdaf91", "#74d17a", "#de1a39", "#0b6c80", "#000000", "#79459f", "#adb6b6"]),
   "lancet_light": np.array(['#f5e1c1', '#8bdb92', '#e05151', '#297787', '#000000', '#9d6ebf', '#adb6b6'])
}


lancet = _liz_palette['lancet']
lancet_light = _liz_palette['lancet_light']


def register_cmap(name=None):
    if not hasattr(register_cmap, "registered"):
        setattr(register_cmap, "registered", False)
    color2rgb = mpl.colors.ColorConverter().to_rgb
    palettes_list = _liz_palette_kv.items()
    if name in _liz_palette_kv:
        palettes_list = [(name, _liz_palette_kv[name])]
    for name, colors in palettes_list:
        cmap = mpl.colors.ListedColormap(list(map(color2rgb, colors.values())), name=name)
        if not register_cmap.registered:
            register_cmap.registered = True
            mpl.colormaps.register(cmap=cmap)


def set_style():
    register_cmap()
    paper_rc = {'lines.linewidth': 5, 'lines.markersize': 15, 'axes.labelweight': 'bold',
                'axes.labelsize': 27, 'axes.titlesize': 27, 'font.size': 25,
                'font.family': 'Arial'}
    sns.set_style('ticks')
    sns.set_context('poster', rc=paper_rc)
    sns.set_palette('lancet')


def lizify(ax: plt.Axes):
    ax.xaxis.get_label().set_fontweight('bold')
    ax.yaxis.get_label().set_fontweight('bold')
    ax.yaxis.grid(visible=True, which="minor", color="#eee", linewidth=1.5)
    ax.yaxis.grid(visible=True, which="major", color='#aaa')


def lineplot(data=None, *, x=None, y=None, 
             hue=None, hue_order=None, ax=None, markers=None, palette=None,
             linewidth=5, markersize=15, alpha=0.8, **kwargs):
    for mm, name in enumerate(hue_order):
        qiepian = data[data[hue] == name]
        if markers is None:
            mkr = 'X'
        else:
            mkr = markers[mm]
        sns.lineplot(qiepian, x=x, y=y, ax=ax, 
                    marker=mkr, label=name, palette=palette,
                    linewidth=linewidth, markersize=markersize, alpha=alpha, **kwargs)
    lizify(ax)


def barplot(data, *, x=None, y=None, hue=None, ax=None, hatches=None, palette=None,
            linewidth=1.5, alpha=1, saturation=1, edgecolor='k', **kwargs):
  sns.barplot(data, x=x, y=y, hue=hue, ax=ax, palette=palette, 
              linewidth=linewidth, alpha=alpha, saturation=saturation, edgecolor=edgecolor, **kwargs)
  if hatches is None:
     return
  if hatches is True:
    hatches = ['..', '||', '--', '//', '++', '\\\\', 'xx', '**']
  for hues, hatch, handle in zip(ax.containers, hatches, ax.get_legend().legend_handles):
      handle.set_hatch(hatch)
      for hue in hues:
          hue.set_hatch(hatch)


def set_mean_bar_label(ax, fontsize=17, fontweight='bold', rotation=90, padding=10, **kwargs):
    for container in ax.containers:
        labels = ['%.2f' % v for v in container.datavalues]
        for i in range(len(container) - 1):
            labels[i] = ''
        ax.bar_label(container, labels=labels, fontsize=fontsize, fontweight=fontweight, 
                     rotation=rotation, padding=padding, **kwargs)


def trimm_mean(df, by, value, lo, hi, outelier_rate=1.5):
    fltr = df.groupby(by).apply(
        lambda x: x[(x[value] <= x[value].min() * outelier_rate)
                    & (x[value] >= x[value].quantile(lo)) 
                    & (x[value] <= x[value].quantile(hi))])
    fltr = fltr.reset_index(drop=True).groupby(by).mean().reset_index()
    return fltr


```

