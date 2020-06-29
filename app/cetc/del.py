# -*- coding: utf-8 -*-


import os

path = r'./1'


def file_name(file_dir):
    jpg_list = []
    json_list = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.jpg':
                jpg_list.append(os.path.splitext(file)[0])
            elif os.path.splitext(file)[1] == '.json':
                json_list.append(os.path.splitext(file)[0])

    diff = set(json_list).difference(set(jpg_list))
    print(len(diff))
    for name in diff:
        print('No jpg:', name + '.json')
        os.remove(path+'/'+name + '.json')

    diff2 = set(jpg_list).difference(set(json_list))
    print(len(diff2))
    for name in diff2:
        print("No json:", name + ".jpg")
        os.remove(path+"/" + name + "*")
    return jpg_list, json_list


file_name(path)
