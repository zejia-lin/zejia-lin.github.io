---
title: "Mac Game Porting Toolkit"
description: ""
excerpt: ""
date: 2024-05-03T17:16:39+08:00
lastmod: 2024-05-03T17:16:39+08:00
draft: false
weight: 50
images: []
categories: []
tags: [mac]
contributors: []
pinned: false
homepage: false
---

This works for me on Mac M1, saved for future reference.

```txt
System: MacOS Sonoma 14.4.1 (23E224)
XCode CLI version: 15.1
Game porting toolkit version: 1.1
```

# Homebrew

This will install `brew` to `/usr/local/bin/brew` even though the M1 version's `brew` is installed in `/opt/homebrew/bin/brew`.

```bash
arch -x86_64 zsh
echo `arch` # should print i386
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Set separate profile for `brew` installation.

```bash
if [ "$(arch)" = "arm64" ]; then
    eval "$(/opt/homebrew/bin/brew shellenv)"
else
    eval "$(/usr/local/bin/brew shellenv)"
fi
```

# Install GPTK

Build from source. This takes 3 hours on my Mac M1. The [Wiki](https://www.applegamingwiki.com/wiki/Game_Porting_Toolkit#Prebuild) also offers a prebuild version to save time.

```bash
brew tap apple/apple http://github.com/apple/homebrew-apple
brew -v install apple/apple/game-porting-toolkit
```

The scripts ends with

```bash
==> game-porting-toolkit
Please follow the instructions in the Game Porting Toolkit README to complete installation.
```

Download the [Game Porting Toolkit](https://developer.apple.com/download/all/?q=game%20porting%20toolkit) redistributable image from Apple. Open the image and copy it into the GPTK directory.

```bash
ditto /Volumes/Game\ Porting\ Toolkit-1.1/redist/lib/ `brew --prefix game-porting-toolkit`/lib/
```

# Initialize Wine

Make directory for Wine to store the Windows stuff. 
This should pop up a Window. 
Change the Windows version to Windows 10.
Note that the `wine64` should be found in `/usr/local/opt/game-porting-toolkit/bin/wine64`.

```bash
mkdir mkdir ~/opt/win10/
WINEPREFIX=mkdir ~/opt/win10/ `brew --prefix game-porting-toolkit`/bin/wine64 winecfg
```

# Install Steeam

Download [Steeam](https://store.steampowered.com/about/download) and install it.

```bash
MTL_HUD_ENABLED=1 WINEESYNC=1 WINEPREFIX=~/opt/win10 /usr/local/opt/game-porting-toolkit/bin/wine64 ~/Downloads/SteamSetup.exe
```

The [Wiki](https://www.applegamingwiki.com/wiki/Game_Porting_Toolkit#Steam_login_black_screen) suggest that using this command to launch Steam. But it doesn't work for me.

```bash
MTL_HUD_ENABLED=1 WINEESYNC=1 WINEPREFIX=~/opt/win10 /usr/local/opt/game-porting-toolkit/bin/wine64 'C:\Program Files/Steam/steam.exe'
```

This works for me.

```bash
WINEPREFIX=~/opt/win10 /usr/local/opt/game-porting-toolkit/bin/wine64 'C:\Program Files/Steam/steam.exe'
```

The Steam login window should appear.


# Reference

- [https://www.applegamingwiki.com/wiki/Game_Porting_Toolkit](https://www.applegamingwiki.com/wiki/Game_Porting_Toolkit)
- [https://github.com/domschl/WinSteamOnMac?tab=readme-ov-file](https://github.com/domschl/WinSteamOnMac?tab=readme-ov-file)
