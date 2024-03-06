---
title: "C++"
description: ""
lead: ""
date: 2023-02-08T17:42:23+08:00
lastmod: 2023-02-08T17:42:23+08:00
draft: false
images: []
menu:
  docs:
    parent: ""
    identifier: "cpp-3ea2e27dc7b3faf9f55aff9a8261dc93"
weight: 999
toc: true
showtitle: true
---

## Split string

```cpp
std::vector<std::string> split(const std::string &s, const std::string &delim=""){
  std::string rr = "\\s+";
  if(delim != ""){
    rr = delim + "+";
  }
  std::regex ws_re(rr); // whitespace
  std::vector<std::string> v(
    std::sregex_token_iterator(str.begin(), str.end(), ws_re, -1),
    std::sregex_token_iterator());
  return v;
}
```

## Binary file IO

```cpp
void readbin(const std::string &filename, void *buffer) {
  std::ifstream fin(filename, std::ios::binary);
  LIZ_CHECKOPEN(fin, filename);
  std::copy(
      std::istreambuf_iterator<char>(fin),
      std::istreambuf_iterator<char>(),
      (char *)buffer);
  fin.close();
}


void readbin_another_way(const std::string &filename, void *buffer){
  std::ifstream fin(filename, std::ios::binary);
  LIZ_CHECKOPEN(fin, filename);
  fin.seekg(0, std::ios::end);
  auto fileSize = fin.tellg();
  fin.seekg(0, std::ios::beg);
  std::cout << fileSize << "\n";
  fin.read(buffer, fileSize);
}

void readbin(const std::string &filename, void *buffer, size_t bytes) {
  std::ofstream fout(filename, std::ios::binary);
  LIZ_CHECKOPEN(fout, filename);
  std::copy(
      (char *)buffer,
      (char *)buffer + bytes,
      std::ostreambuf_iterator<char>(fout));
  fout.close();
}

```

## Macros

- Identifier with line number
  ```cpp
  #define CAT_(a, b) a ## b
  #define CAT(a, b) CAT_(a, b)
  #define VARNAME(Var) CAT(Var, __LINE__)
  ```
