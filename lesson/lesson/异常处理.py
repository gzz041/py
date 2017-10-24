#!/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "Gao"

class MyselfException(Exception):
    '''
    这是一个自己定义的异常，
    需要继承Exception这个基类
    '''
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message
        # return '最好是写self.message'

try:
    # 这里就调用自定义的异常，一般是要结合那些判断啊，循环什么的，这样写，没实质性卵用
    raise MyselfException('这是我的地盘！')
except MyselfException as e:
    print('!!!到except了!!!', e)