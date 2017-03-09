#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 实践configparser
# 读取ini, conf文件

# 导入ConfigParser包
import configparser


# 1. ConfigParser()
# 2. RowConfigParser()
# 3. BaseConfigParser()
if __name__ == '__main__':

    configfile = 'configparser_practice.ini'
    # 取得一个configParser对象
    cf = configparser.ConfigParser()
    cf.read(configfile)

    ########### 读取 ###########
    # 读取配置文件,返回配置文件的段，list
    sections = cf.sections()
    print(sections)    # => ['sec_a', 'sec_b']

    # 选取其中一个段
    opts = cf.options('sec_a')
    # 返回这个段的key，list
    print(opts)        # => ['a_key1', 'a_key2']

    # 按section，key取得值，默认str
    str_val = cf.get('sec_a', 'a_key1')
    # 取int值
    int_val = cf.getint('sec_a', 'a_key2')
    print(str_val, int_val) # => 20 10

    ########### 更新 ###########
    # 按section，key更新值
    cf.set('sec_b', 'b_key3', 'new-$r')
    # 其实是在内存里更新，并没有flush到文件
    print(cf.get('sec_b', 'b_key3'))
    # 新建一个key:value
    cf.set('sec_b', 'b_newkey', 'new-value')
    # 新建一个段(若存在会报错)
    if not cf.has_section('a_new_section'):
        cf.add_section('a_new_section')
    cf.set('a_new_section', 'new_key', 'new_value')

    # 写入
    cf.write(open(configfile, 'w'))

    ########### 使用 rawConfigParser ###############
    rcf = configparser.RawConfigParser()
    rcf.read(configfile)

    # 对%(host)的变量不转义，原文输出
    print(rcf.get('portal', 'url'))     # http://%(host)s:%(port)s/Portal
    # 新建一个key:value
    rcf.set('portal', 'url2', '%(host)s:%(port)s')
    # 对%(host)的变量不转义，原文写入
    print(rcf.get('portal', 'url2'))    # %(host)s:%(port)s

    ########### 使用 configParser ###############
    cf1 = configparser.ConfigParser()
    cf1.read(configfile)

    # 对%(host)的变量转义后输出
    print(cf1.get('portal', 'url'))     # http://localhost:8080/Portal
    # 新建一个key:value
    cf1.set('portal', 'url2', '%(host)s:%(port)s')
    # 对%(host)的变量转义后写入
    print(cf1.get('portal', 'url2'))    # localhost:8080

    ########### 使用 safeConfigParser ###############
    # 同ConfigParser
    scf = configparser.SafeConfigParser()
    scf.read(configfile)

    # 对%(host)的变量转义后输出
    print(scf.get('portal', 'url'))     # http://localhost:8080/Portal
    # 新建一个key:value
    scf.set('portal', 'url2', '%(host)s:%(port)s')
    # 对%(host)的变量转义后写入
    print(scf.get('portal', 'url2'))    # localhost:8080

    # 创建一个重复sectoin会出错
    if not scf.has_section('a_new_section'):
        scf.add_section('a_new_section')
