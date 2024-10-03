from diff import  *


if __name__ == '__main__':
    # with open('dump.sql', 'r',encoding='utf-8') as file:
    #     lines = file.readlines()
    #     full_text = ''.join(lines)
    #     find_createTableAndCopy(full_text)
    find_tableAndKey()
    find_diff()


