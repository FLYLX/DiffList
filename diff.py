import re

def find_createTableAndCopy(full_text):
    pattern = re.compile(r'CREATE TABLE.*?\);', re.DOTALL | re.MULTILINE)
    pattern1 = re.compile(r'COPY\s+.*?\s+.*?\\\.', re.DOTALL | re.MULTILINE)
    matches = pattern.findall(full_text)
    matches1 = pattern1.findall(full_text)
    with open('output_createTableAndCopy.txt', 'w',encoding='utf-8') as output_file:
        for match in matches:
            output_file.write(match + '\n')  # 将每个匹配项写入文件，并在末尾添加换行符
        for match in matches1:
            output_file.write(match + '\n')  # 将每个匹配项写入文件，并在末尾添加换行符

def find_tableAndKey():
    with open('mx_17.txt', 'r', encoding='utf-8') as file:
        lines1 = file.readlines()
        for line in lines1:
            with open('output_tableAndKey.txt', 'a',encoding='utf-8') as output_file:
                    if line.startswith('key'):
                        table_value = line.split(' ', 1)[1].split(' ')[0]
                        last_value = line.rsplit(' ', 1)[1]
                        output_file.write(table_value+' ')  # 将每个匹配项写入文件，并在末尾添加换行符
                        output_file.write(last_value)  # 将每个匹配项写入文件，并在末尾添加换行符
                    elif line.startswith('table'):
                        key_value = line.split(' ', 1)[1].split(' ')[0]
                        output_file.write(key_value+'\n')  # 将每个匹配项写入文件，并在末尾添加换行符

def find_diff():
    table_list = {}
    with open('output_tableAndKey.txt', 'r', encoding='utf-8') as file:
        lines1 = file.readlines()
        for line in lines1:
            stripped_line = line.strip()
            if ' ' in line :
                before_space_string , after_space_string = stripped_line.split(' ', 1)
                table_list.setdefault(after_space_string,[]).append(before_space_string)
    print(table_list)
    return table_list
