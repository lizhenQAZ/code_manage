import difflib


print(">"*20, " 比较字符串差异 ", "<"*20)
text1 = """text1:
This module provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.4
add string
"""
text2 = """text2:
This module provides classes and functions for Comparing sequences.
including HTML and context and unified diffs.
difflib document v7.5
"""
text1_lines = text1.splitlines()
text2_lines = text2.splitlines()
# print("="*20, " 生成text对比文件", "="*20)
# d = difflib.Differ()
# diff = d.compare(text1, text2)
# print("\n".join(list(diff)))

print("="*20, " 生成HTML对比文件", "="*20)
d = difflib.HtmlDiff()
diff = d.make_file(text1, text2)
print(diff)
