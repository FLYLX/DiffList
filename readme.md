运行之前,output_tableAndKey.txt 文件保持清空，因为是在文件尾追加内容
dump.sql 是 17，输出为 output_createTableAndCopy.txt，是只显示 create 和 copy 的 sql 语句

主要保证 mx_17 里面是栋哥的工具导出的差异语句， diff.py 中的find_tableAndKey然后再find_diff，即可返回一个字典，里面有关于table中的差异字段
