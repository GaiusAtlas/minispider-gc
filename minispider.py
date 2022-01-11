#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

#########################################################
#
# Copyright (c) 2022 Baidu.com, Inc. All Rights Reserved
#
#########################################################

'''
minispier
'''

import os
import argparse    # 字符串处理库
import conf_load   # 载入配置文件

def parse_args():
    parser = argparse.ArgumentParser(description='To get spider configuration.')
    parser.add_argument('--conf', '-c', help='get config file',required=True)
    parser.add_argument('--integers', '-i', type=int, nargs='+', help='传入的数字')
    args_p = parser.parse_args()
    return args_p


if __name__ == '__main__':
    try:
        args = parse_args()
        conf_load.get_conf(args.conf)
    except Exception as e:
        print(e)