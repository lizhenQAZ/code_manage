import filecmp


print(">"*20, " 比较目录差异 ", "<"*20)
print("="*20, " 比较单文件差异 ", "="*20)
print("两个文件相同: ", filecmp.cmp("./nginx.conf.v1", "./nginx.conf.v2"))

print("="*20, " 比较多文件差异 ", "="*20)
print("多文件对比结果([‘匹配’], [‘不匹配’], [‘错误’])：", filecmp.cmpfiles("../01_basic_info",
                                                            "../02_service_monitor", ['f1', 'f2', 'f3']))

print("="*20, " 比较目录差异 ", "="*20)
dir_diff = filecmp.dircmp("../01_basic_info", "../02_service_monitor")
print("比较指定目录内容: ", dir_diff.report())
print("比较指定目录和第一级子目录内容: ", dir_diff.report_partial_closure())
print("比较所有指定目录内容: ", dir_diff.report_full_closure())
print("只在左侧目录的文件及目录列表: ", dir_diff.left_list)
print("只在右侧目录的文件及目录列表: ", dir_diff.right_list)
print("两边目录都存在的子目录: ", dir_diff.common)
print("只在左侧目录的文件或目录: ", dir_diff.left_only)
print("只在右侧目录的文件或目录: ", dir_diff.right_only)
print("两边目录都存在的子目录: ", dir_diff.common_dirs)
print("两边目录都存在的子文件: ", dir_diff.common_files)
print("两边目录都存在的子目录(目录类型和错误): ", dir_diff.common_funny)
print("匹配相同文件: ", dir_diff.same_files)
print("不匹配文件: ", dir_diff.diff_files)
print("两边都存在无法比较的文件: ", dir_diff.funny_files)
print("将common_dirs映射为新的dircmp对象: ", dir_diff.subdirs)

