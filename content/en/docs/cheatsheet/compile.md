---
title: "Compilation"
description: ""
lead: ""
date: 2023-01-12T18:34:30+08:00
lastmod: 2023-01-12T18:34:30+08:00
draft: false
images: []
menu:
  docs:
    parent: "cheatsheet"
    identifier: "cmake-e79db5acb8541c26322a00eba56428c5"
weight: 999
toc: true
showtitle: false
---

# GDB

## Debugging LLVM OPT

```bash
# Run gdb
gdb opt
# Set breakpoint
break llvm::Pass::preparePassManager
# Run pass
run -load ./mypass.so -hello < hello.bc > debug.log
```

# Clang

## Clang Get IR

```bash
clang -S -emit-llvm
```

## CUDA Related

Compiling CUDA with clang: [official document](https://llvm.org/docs/CompileCudaWithLLVM.html), in short:

```bash
clang++ helloworld.cu -o helloworld --cuda-gpu-arch=<arch> \
  -L<CUDA install path>/<lib64 or lib>                     \
  -lcudart_static -ldl -lrt -pthread
```


# Linker

## GLIBCXX

Check if a string exists in the shared library

```bash
strings libstdc++.so.6 | grep GLIBCXX
```

## Linker Arguments

- The arguments could be passed to linker by `clang -Wl,<comma seperated args>`,for example, `clang -Wl,-rpath,<a> -Wl,-rpath,<b>`.
- `-rpath <path>`: has the same effect as setting the `LD_LIBRARY_PAH`, but specifies it at link time.
- `-dynamic-linker`: specifies the dynamic linker, see a good [tutorial for dynamic linking](https://developer.ibm.com/tutorials/l-dynamic-libraries/) 


