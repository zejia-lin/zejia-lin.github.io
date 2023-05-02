---
title: "Llvm GEP Explained"
description: ""
excerpt: "Q: Why dose GEP has an extra 0 operand? <br> A: Pointer and ArrayType is not the same in LLVM."
date: 2023-02-06T18:55:38+08:00
lastmod: 2023-02-06T18:55:38+08:00
draft: false
weight: 50
images: []
categories: []
tags: ['llvm']
contributors: ["Zejia Lin"]
pinned: false
homepage: false
---

# Why 0 in GEP

为什么生成的GEP会的第一个参数是0呢？[官方文档](https://llvm.org/docs/GetElementPtr.html)过于晦涩，[这篇博客](https://blog.yossarian.net/2020/09/19/LLVMs-getelementptr-by-example)很好的解释了这个问题。

```cpp
long nums[] = {1, 2, 3};
long i;
long index_i(void) {
  return nums[i];
}
```

```cpp
@nums = dso_local global [3 x i64] [i64 1, i64 2, i64 3], align 16
@i = common dso_local global i64 0, align 8

define dso_local i64 @index_i() #0 {
  %0 = load i64, i64* @i, align 8
  %arrayidx = getelementptr inbounds [3 x i64], [3 x i64]* @nums, i64 0, i64 %0
  %1 = load i64, i64* %arrayidx, align 8
  ret i64 %1
}
```

简单来说数组和指针在LLVM里是严格区分的，不可以用C语言的方式来理解。传给GEP的参数必须是指针，因此实际上传的是指向数组的指针，因此索引方式为`(&nums)[0][i]`，第一个0表示了数组地址。

# How to use in IRBuilder

需要注意GEP返回的是一个指针，要用load或者store来使用

```cpp
llvm::Type *elmType = ...;
llvm::ArrayType *arrayType = ...;
llvm::Value *array = ...;
size_t index = ...;
auto gep = builder.CreateGEP(arrayType, array, 
              {builder.getInt64(0), builder.getInt64(index)});
auto elm = builder.CreateLoad(elmType, gep);
... // do what you want with elm
```

同理的一个坑，如果一个C语言函数接受一个指针，在IR里传入的参数也需要用GEP来获取首地址

```cpp
// Function signature
void func(int *array);

// LLVM code
auto gep = builder.CreateGEP(arrayType, array, 
              {builder.getInt64(0), builder.getInt64(0)});
auto ret = builder.CreateCall(func, gep);
```

