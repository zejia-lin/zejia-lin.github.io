---
title: "Cmake"
description: ""
lead: ""
date: 2023-02-26T12:58:14+08:00
lastmod: 2023-02-26T12:58:14+08:00
draft: false
images: []
menu:
  docs:
    parent: ""
    identifier: "cmake-5b26d22cb8b5a7ace8439150a50264ce"
weight: 999
toc: true
showtitle: false
---

# Variables

## Tutorial

- https://cliutils.gitlab.io/modern-cmake/

## Directory Variables

- `CMAKE_SOURCE_DIR`: Top-level `CMakeLists.txt` file's dir.
- `CMAKE_CURRENT_SOURCE_DIR`: This `CMakeLists.txt` files' dir.
- `PROJECT_SOURCE_DIR`: Most recent `CMakeLists.txt` file that defines a project
- *`projectName`*`_SOURCE_DIR`: Directory of the *`projectName`*
- For binary directories, replace `SOURCE` with `BINARY`


# Snippets

## Iterate all targets

https://stackoverflow.com/questions/37434946/how-do-i-iterate-over-all-cmake-targets-programmatically

```cmake
function(get_all_targets var)
    set(targets)
    get_all_targets_recursive(targets ${CMAKE_CURRENT_SOURCE_DIR})
    set(${var} ${targets} PARENT_SCOPE)
endfunction()

macro(get_all_targets_recursive targets dir)
    get_property(subdirectories DIRECTORY ${dir} PROPERTY SUBDIRECTORIES)
    foreach(subdir ${subdirectories})
        get_all_targets_recursive(${targets} ${subdir})
    endforeach()

    get_property(current_targets DIRECTORY ${dir} PROPERTY BUILDSYSTEM_TARGETS)
    list(APPEND ${targets} ${current_targets})
endmacro()

get_all_targets(all_targets)
message("All targets: ${all_targets}")
```

## Custom commands

https://dev.to/iblancasa/learning-cmake-3-understanding-addcustomcommand-and-addcustomtarget-43gp
