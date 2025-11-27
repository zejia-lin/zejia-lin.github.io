---
title: "Llvm Indirect Call"
description: "LLVM `call` vs `invoke`, and handling indirect call"
excerpt: "LLVM call vs invoke, and handling indirect call"
date: 2023-02-04T17:28:38+08:00
lastmod: 2023-02-04T17:28:38+08:00
draft: true
weight: 50
images: []
categories: []
tags: []
contributors: ["Zejia Lin"]
pinned: false
homepage: false
toc: true
---

# Records Answers from ChatGPT

I found few infomation about the difference between LLVM `call` and `invoke` instruction, so I turn to ChatGPT and it provides the following answer. I have no ensurance on the correctness but just records it.

### What's the difference between a LLVM Call and Invoke

In LLVM, "Call" and "Invoke" are two different instructions used to call functions.

"Call" is used to make a normal function call. The function is executed and control is returned to the caller once the function returns.

"Invoke" is used to make a function call that can throw an exception. In addition to the normal function call, "Invoke" provides a way to handle exceptions by specifying a "normal destination" and an "unwind destination". If the function throws an exception, control is transferred to the unwind destination; otherwise, control is transferred to the normal destination after the function returns.

In summary, "Call" is for normal function calls, while "Invoke" is for function calls that can throw exceptions and provides a way to handle them.

### How can I deal with "Invoke" in IR builder

To deal with "Invoke" instructions in LLVM IR builder, you can use the CreateInvoke method of the IRBuilder class. Here is an example, note that the `CreateInvoke` method returns a `CallInst` object, which is a subclass of Instruction that represents an "Invoke" instruction.

```cpp
FunctionType *FT = ...;
Value *Callee = ...;
std::vector<Value *> Args = ...;
BasicBlock *NormalDest = ...;
BasicBlock *UnwindDest = ...;

IRBuilder<> Builder(...);
Builder.CreateInvoke(FT, Callee, NormalDest, UnwindDest, Args);
```

### Can I treat "Call" and "Invoke" as the same in a LLVM pass

In a LLVM pass, you can treat "Call" and "Invoke" as the same to some extent. Both "Call" and "Invoke" are represented by the CallInst class in LLVM, which is a subclass of the Instruction class. This means that you can manipulate both "Call" and "Invoke" instructions using the same set of methods and interfaces provided by the Instruction class and its subclasses.

However, it's important to remember that "Call" and "Invoke" have different semantics and behaviors, so it's essential to distinguish between them when you're performing certain operations, such as analyzing the control flow of a program.

For example, if you're writing a pass that deals with function calls, you might need to check if an instruction is a "Call" or an "Invoke", and then handle them differently. You can do this by using the isCall method or the isInvoke method of the Instruction class, which return true if the instruction is a "Call" or an "Invoke", respectively.

Here is an example of how you can use these methods in a LLVM pass:

```cpp
for (Instruction &I : instructions(F)) {
  if (CallInst *CI = dyn_cast<CallInst>(&I)) {
    if (CI->isCall()) {
      // Handle Call instruction
    } else if (CI->isInvoke()) {
      // Handle Invoke instruction
    }
  }
}
```

### What happens if a CallInst.getCalledFunction returns nullptr

In LLVM, if a CallInst's getCalledFunction method returns nullptr, it means that the target of the call is not a known function. This could occur in several scenarios, such as:

- The call target is an indirect function call, meaning that the function address is stored in a memory location or register and is loaded dynamically at runtime.
- The call target is a function pointer stored in a global variable or another register.
- The call target is a function that is defined in another module or a dynamically linked library and is not present in the current module.

In these cases, the compiler cannot determine the exact function that will be called at runtime, so it cannot perform optimizations such as inlining or constant propagation. To handle these situations, LLVM provides a mechanism called "Indirect Call Promotion" that can transform indirect calls into direct calls to a small set of candidate functions.

If you're writing a pass that needs to manipulate function calls, it's important to check if the call target is a known function and handle indirect calls appropriately.
