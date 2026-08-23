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

Check if there is Type 3 font in PDF.

```python
import os
import subprocess
import sys

def check_pdffonts_installed():
    """检查系统是否安装了 pdffonts 工具"""
    try:
        subprocess.run(["pdffonts", "-v"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False

def has_type3_font(file_path):
    """
    使用 pdffonts 检查单个 PDF 文件是否包含 Type 3 字体。
    返回: (bool, list) -> (是否包含, 字体信息列表)
    """
    try:
        # 调用 pdffonts 命令
        result = subprocess.run(
            ["pdffonts", file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8', # 防止中文路径或内容乱码
            errors='ignore'
        )
        
        if result.returncode != 0:
            print(f"[Error] 无法读取文件: {file_path}")
            return False, []

        lines = result.stdout.splitlines()
        type3_fonts = []
        found_type3 = False

        # 跳过前两行（标题行）
        # name type encoding emb sub uni object ID
        for line in lines[2:]:
            # 检查每一行是否包含 "Type 3"
            # 注意：pdffonts 的输出格式中，Type 列通常是 "Type 3"
            if "Type 3" in line:
                found_type3 = True
                type3_fonts.append(line.strip())

        return found_type3, type3_fonts

    except Exception as e:
        print(f"[Exception] 处理文件出错 {file_path}: {e}")
        return False, []

def scan_directory(directory):
    """遍历目录并检查 PDF"""
    print(f"正在扫描目录: {directory} ...\n")
    
    pdf_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".pdf"):
                pdf_files.append(os.path.join(root, file))

    if not pdf_files:
        print("未找到 PDF 文件。")
        return

    count_bad = 0
    bad_files = []

    for pdf_path in pdf_files:
        is_bad, fonts = has_type3_font(pdf_path)
        if is_bad:
            count_bad += 1
            bad_files.append(pdf_path)
            print(f"❌ 发现 Type 3: {pdf_path}")
            # 如果你想看具体是哪个字体，取消下面这行的注释
            # for f in fonts: print(f"    -> {f}")
        else:
            # 只有在想看所有文件状态时才取消注释下面这行
            # print(f"✅ 通过: {pdf_path}")
            pass

    print("-" * 50)
    print(f"扫描完成。共检查 {len(pdf_files)} 个文件。")
    if count_bad > 0:
        print(f"发现 {count_bad} 个文件包含 Type 3 字体：")
        for f in bad_files:
            print(f" - {f}")
    else:
        print("完美！所有文件中均未发现 Type 3 字体。")

if __name__ == "__main__":
    # 检查 pdffonts 是否存在
    if not check_pdffonts_installed():
        print("错误: 未找到 'pdffonts' 命令。")
        print("请先安装 Poppler utils (Windows/Mac/Linux) 并确保添加到环境变量 PATH 中。")
        sys.exit(1)

    # 获取目标文件夹路径
    target_dir = "."
    if len(sys.argv) > 1:
        target_dir = sys.argv[1]
    
    scan_directory(target_dir)
```
