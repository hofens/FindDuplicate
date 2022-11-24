import os


def write_list_to_file(file_path, source_list):
    result_txt = open(file_path, 'w+', encoding='utf-8')
    for key in source_list:
        result_txt.write(key + "\n")
    result_txt.close()
    return os.path.abspath(file_path)


def list_convert_from_txt(path):
    result = []
    file = open(path, 'r', encoding='utf-8')
    for line in file:
        result.append(line.replace("\n", ""))
    return result