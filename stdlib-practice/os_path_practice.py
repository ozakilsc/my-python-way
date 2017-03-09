#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# os.path的用法
# 路径操作，基本文件判断
import os
import pprint

pp = pprint.pprint
# pp(os.path.__dict__)

if __name__ == '__main__':
    ########## 取环境变量 ##########
    gopath = os.getenv('GOPATH')
    # 若取不到，给个默认值
    u = os.getenv('USERNAME', 'Smith')
    print(gopath, u)

    ########## 处理文件路径 ##########
    # 当前路径
    print(os.path.curdir)       # '.'
    # 返回绝对路径: 在当前cwd目录下加上一个尾巴(不判断存不存在)
    print(os.path.abspath('abc'))
    # 返回绝对路径: 支持相对路径表达，在当前cwd目录下加上一个尾巴(不判断存不存在)
    print(os.path.abspath('../../abc'))
    # 分离地址为一个元组，(目录, 文件名)
    print(os.path.split('/ab/c/d/e'))       # ('/ab/c/d', 'e')
    # 分离磁盘驱动器,返回一个2个元素的元组
    print(os.path.splitdrive('d:\\new\\hello.txt')) # 返回（drivername，fpath）元组
    # 分离文件扩展名,返回一个2个元素的元组
    print(os.path.splitext('d:\\new\\hello.txt'))   # ('d:\\new\\hello', '.txt')
    # 返回split元组的第一个元素
    print(os.path.dirname('/ab/c/d/e'))
    # 返回split元组的第二个元素                 # /ab/c/d
    print(os.path.basename('/ab/c/d/e'))    # e
    # 返回共有的路径前缀， 接受一个list参数
    print(os.path.commonprefix(['/ab/c/d/e', '/ab/c/d', '/ab/c/d/e/f/g/h']))
    # 判断路径是否存在
    print(os.path.exists('c://'))           # False
    # 判断路径是否存在 如果文件是链接，即使链接broken了，也返回True。l: link
    print(os.path.lexists('/ab/c/d/e'))
    # 判断是否绝对路径(不判断存不存在)
    print(os.path.isabs('/ab/c/d/e'))       # True
    # 判断是否是文件，会判断是否存在
    print(os.path.isfile('/ab/c/d/e'))      # False
    # 判断是否是目录，会判断是否存在
    print(os.path.isdir('/ab/c/d/e'))       # False
    # 判断是否是链接，会判断是否存在
    print(os.path.islink('/ab/c/d/e'))       # False
    # 判断路径是否为挂载点
    print(os.path.ismount('/Volumes/HD'))               # False
    # 路径连接，不判断存不存在
    print(os.path.join('a','b','c'))        # a/b/c
    # 路径连接, 自动取最深的路径
    print(os.path.join('/home/aa','/home/aa/bb','/home/aa/bb/c')) # /home/aa/bb/c
    print(os.path.join('/home/aa','/home/aa/bb','/home/aa/bd/c')) # /home/aa/bd/c
    # 将'~'改为绝对路径
    print(os.path.expanduser('~/iga'))      # /Users/#{username}/iga
    # 根据环境变量的值替换path中包含的”$name”和”${name}”
    print(os.path.expandvars('/a/b$GOPATH${GOPATH}'))
    # Linux和Mac: 原样返回path; windows: 路径中所有字符转换为小写，所有反斜杠转换为斜杠
    print(os.path.normcase('/ab/c/d/e'))
    # 规范路径表达，去掉双斜杠
    print(os.path.normpath('/ab/c/d/e'))
    # 当前文件名
    print(__file__)
    # 文件的大小, 值从os.stat()的st_size里来, byte
    print(os.path.getsize(os.path.basename(__file__)))  # 2285
    print(os.stat(__file__))
    # 最后一次访问时间(float)，值从os.stat()的st_atime(int)里来   attach time
    print(os.path.getatime(__file__))                   # 1489048492.0
    # 最后一次修改时间(float)，值从os.stat()的st_mtime(int)里来   modify time
    print(os.path.getmtime(__file__))                   # 1489048492.0
    # 创建时间(float)，值从os.stat()的st_ctime(int)里来          create time
    print(os.path.getctime(__file__))                   # 1489048492.0
    # 转为相对路径，不判断存不存在。若不存在则从当前路径到根路径/算起，否则从cwd算起
    print(os.path.relpath('/ab/c/d/e'))                 # ../../../../../../../ab/c/d/e
    # 转为绝对路径，不判断存不存在。
    print(os.path.realpath('../c/d/e'))                 # /Users/${username}/iga/workspace/py-yard/my-pyhon-way/c/d/e
    # 判断目录文件是否相同(str, str)，若不存在会exception
    print(os.path.samefile(__file__, __file__))
    # write方式打开文件，若不存在会创建, 不支持相对路径
    # f_fp1 = open(os.path.join(os.getcwd(), 'test_file_1'), 'w')
    # f_fp2 = open(os.path.join(os.getcwd(), 'test_file_2'), 'w')
    fp1 = os.path.join(os.getcwd(), 'test_file_1')  # 绝对路径
    print(os.path.relpath(fp1))     # 取相对路径
    # 判断是否指向同一个文件
    # print(os.path.sameopenfile(os.path.relpath(fp1), fp1))  # todo 测试失败
    # f_fp1 = open(os.path.join(os.getcwd(), 'test_file_1'), 'r')
    # f_fp2 = open(os.path.join(os.getcwd(), 'test_file_2'), 'r')
    # 判断是否指向同一个文件
    # print(os.path.samestat(f_fp1, f_fp2))                   # todo 测试失败




