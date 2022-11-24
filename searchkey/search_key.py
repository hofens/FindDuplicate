# coding=utf-8
"""
    检索关键字是否存在文件中
"""

# -*- coding: utf-8 -*-
import os
import re
import json


def print_hi(name):
    print("读取文件, {0}".format(name))


# 从json文件中获取 字符串列表
def set_convert_from_json(file):
    with open(file, encoding='utf-8') as a:
        result = json.load(a)
        keyList = re.findall(r"'key': '(\w*)'", str(result))
        print(keyList)
        return set(keyList)


# 从txt文件中获取 字符串列表
def list_convert_from_txt(path):
    result = []
    file = open(path, 'r', encoding='utf-8')
    for line in file:
        result.append(line.replace("\n", ""))
    return result


# 获取需要检查的文件，排除非java、kt后缀的文件
def get_files(root_path):
    file_list = []
    for i in os.listdir(root_path):
        path = root_path + r'\\' + i
        if os.path.isfile(path):
            if path.endswith("java") or path.endswith("kt"):
                print("当前检测文件 " + path)
                file_list.append(path)
        elif os.path.isdir(path):
            files = get_files(path)
            for f in files:
                if f.endswith("java") or f.endswith("kt"):
                    file_list.append(f)
    return file_list


# 遍历每个文件，找出在左右文件中未出现的字符串
def str_not_exist_in_files(root_path, words, result_file_name, output_dir_name):
    file_list = get_files(root_path)
    used_words = set()
    # 找到所有使用的word
    for path in file_list:
        print_hi(path)
        for word in words:
            if word in open(path, 'r', encoding='utf-8').read():
                used_words.add(word)
    # 获取未使用的word
    unused_words = set(set(words).difference(set(used_words)))

    result_txt = open('dev/unused_key_result_{0}.txt'.format(result_file_name), 'w+', encoding='utf-8')
    result_txt.write("all_key_num: {0} contain_key_num: {1} unused_key_num: {2} \n".format(len(words), len(used_words),
                                                                                           len(unused_words)))
    result_txt.write("contain_key {0} \n\n".format(used_words))
    result_txt.write("unused_key: \n".format(used_words))

    for word in unused_words:
        result_txt.write(word + '\n')
    result_txt.close()

    print("\n all_key {0} contain_key {1} unused_key {2}".format(len(words), len(used_words), len(unused_words)))
    print("\n unused_key {0}".format(unused_words))

    return unused_words


def check_all_project_unused_key(json_file, output_dir_name):
    all_key = set_convert_from_json(json_file)
    cc_unused_key = str_not_exist_in_files(r'F:\tempProjects\cc', all_key, 'cc', output_dir_name)
    ccaudio_unused_key = str_not_exist_in_files(r'F:\tempProjects\ccaudiolive', cc_unused_key, 'ccaudio', output_dir_name)
    ccdsroomsdk_unused_key = str_not_exist_in_files(r'F:\StudioProjects\ccdsroomsdk', ccaudio_unused_key, 'ccdsroomsdk', output_dir_name)
    CCRecordLive_unused_key = str_not_exist_in_files(r'F:\StudioProjects\CCRecordLive', ccdsroomsdk_unused_key,
                                                     'CCRecordLive', output_dir_name)
    ccrecordlivesdk_unused_key = str_not_exist_in_files(r'F:\StudioProjects\ccrecordlivesdk', CCRecordLive_unused_key,
                                                        'ccrecordlivesdk', output_dir_name)
    cclivecar_unused_key = str_not_exist_in_files(r'C:\Users\N22117\Projects\cclivecar', ccrecordlivesdk_unused_key,
                                                  'cclivecar', output_dir_name)
    CCGRoomSDK_unused_key = str_not_exist_in_files(r'C:\Users\N22117\StudioProjects\CCGRoomSDK', cclivecar_unused_key,
                                                   'CCGRoomSDK', output_dir_name)
    LanProjectionScreenSDK_unused_key = str_not_exist_in_files(r'F:\StudioProjects\LanProjectionScreenSDK',
                                                               CCGRoomSDK_unused_key, 'LanProjectionScreenSDK', output_dir_name)
    cui_unused_key = str_not_exist_in_files(r'F:\StudioProjects\cui', LanProjectionScreenSDK_unused_key, 'cui', output_dir_name)


