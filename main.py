
# coding=utf-8
# -*- coding: utf-8 -*-


from searchkey.search_key import *


if __name__ == '__main__':
    # get_all_project_unused_key('searchkey/data/appconfig.json', 'release')
    rel_key = set_convert_from_json('searchkey/data/appconfig.json')
    dev_key = set_convert_from_json('searchkey/data/appconfig_dev.json')

    print("\n all_key {0} all_dev_key {1}".format(len(rel_key), len(dev_key)))
    #
    # # 内网有，外网没有的
    # dev_extra = dev_key.difference(rel_key)
    # print("多余的 {0}".format(len(dev_extra)))
    #
    # # result_txt = open('searchkey/dev/dev_extra.txt', 'w+', encoding='utf-8')
    # # for key in dev_extra:
    # #     result_txt.write(key +"\n")
    # # result_txt.close()
    #
    # unused_key = list_convert_from_txt('searchkey/dev/dev_unused_result.txt')
    # res = list(set(unused_key) & set(dev_extra))
    #
    # result_txt = open('searchkey/del_unused_and_extra.txt', 'w+', encoding='utf-8')
    # for key in res:
    #     result_txt.write(key +"\n")
    # result_txt.close()
    #
    # print(res)


