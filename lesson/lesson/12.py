#!/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "Gao"

import subprocess

sub = subprocess

# sub.run(r"ls -ll", shell=True)  # 这条命令在Linux环境下用
# sub.run('dir')
sub.run(r'dir', shell=True)  # 这条命令在Win环境下用

