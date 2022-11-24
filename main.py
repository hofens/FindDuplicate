
# coding=utf-8
# -*- coding: utf-8 -*-


from searchkey.search_key import *
from utils import file_helper

if __name__ == '__main__':
    # get_all_project_unused_key('searchkey/data/外网appconfig配置.json', 'release')
    rel_key = set_convert_from_json('searchkey/data/appconfig.json')
    dev_key = set_convert_from_json('searchkey/data/appconfig_dev.json')

    print("\n all_key {0} all_dev_key {1}".format(len(rel_key), len(dev_key)))
    # 内网有，外网没有的
    only_dev_config = dev_key.difference(rel_key)
    # 内网没有，外网有的
    only_release_config = rel_key.difference(dev_key)

    # 代码中没有声明的
    unused_in_codes = file_helper.list_convert_from_txt('searchkey/dev/dev_unused_result.txt')
    file_helper.write_list_to_file('searchkey/data/unused_in_codes.txt', unused_in_codes)
    # 内网有配置,代码中有声明的
    in_config_and_code = only_dev_config.difference(unused_in_codes)
    file_helper.write_list_to_file('searchkey/data/in_config_and_code.txt', in_config_and_code)
    # 内网有配置,代码中没有声明的
    in_config_without_code = list(set(only_dev_config) & set(unused_in_codes))
    file_helper.write_list_to_file('searchkey/data/in_config_without_code.txt', in_config_without_code)



