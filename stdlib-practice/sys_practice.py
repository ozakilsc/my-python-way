#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# os.path的用法
# 路径操作，基本文件判断
import sys
import pprint

pp = pprint.pprint
# pp(sys.__dict__)

if __name__ == '__main__':
    # 当前文件路径list，当前文件为sys.argv[0]
    print(sys.argv)
    # 当前python版本信息
    print(sys.version)
    # real最大值
    print(sys.maxsize.real)
    # 模块搜索路径list(当前 > env: PYTHONPATH > PYTHONdir(.pth) > site-package(.pth))
    print(sys.path)
    # darwin
    print(sys.platform)
    # 向stdout写入，没有\n
    sys.stdout.write('please')
    # 读取stdin的输入,会产生阻塞等待用户输入
    val = sys.stdin.readline()[:-1]
    print(val)
    # 正常退出程序
    print(sys.exit(0))
    