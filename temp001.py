#!/usr/bin/env python
# _*_coding:utf-8_*_
# author : gaozhizhong

import json
from prettytable import PrettyTable

user_account = {
    '路人甲': '123456',
    '路人乙': '123456',
    '路人丙': '123456',
    '路人丁': '123456',
}
user_info = {
    '路人甲': {"工资": 20000, '余额': 20000, '购物车': []},
    '路人乙': {"工资": 10000, '余额': 10000, '购物车': []},
    '路人丙': {"工资": 5000, '余额': 5000, '购物车': []},
    '路人丁': {"工资": 2000, '余额': 2000, '购物车': []},
}

product_info = {
    '001': {'货名': 'iphone', '货价': 5888, },
    '002': {'货名': 'Mac Pro', '货价': 12000, },
    '003': {'货名': 'Coffe', '货价': 31,},
    '004': {'货名': 'Python Alex', '货价': 120, },
}
product_list = [
    '货号：001 商品：iphone 价格：5888',
    '货号：002 商品：Mac Pro 价格：12000',
    '货号：003 商品：Coffe 价格：31',
    '货号：004 商品：Python Alex 价格120',
]

def loggin(user_name):
    """
    定义一个用户登录认证函数
    如果你把认证的用户及密码写到该函数中效果就会更好，节省了代码，返回值为字符串最好不要作为判断的条件
    """
    user_passwd = input("用户密码：\n")

    if len(user_name) == 0 or user_name not in user_account:
        return False
    elif user_name in user_account and user_passwd == user_account[user_name]:
        return user_name


def print_product_list():
    """
    定义个打印产品列表
    """
    for goods in product_list:
        print(goods)


def fetch(user_name):
    """
    查询已购买商品，打印货品名
    :param user_name:     用户名
    :return:
    """
    print(user_name,'工资:',user_info[user_name]['工资'])
    print(user_name, '余额:', user_info[user_name]['余额'])
    print(user_name, '购物车:', user_info[user_name]['购物车'])


def buy(user_name,*user_salary):
    """
    购物商城主逻辑去
    :param user_name:      用户名
    :param user_salary:    用户钱数(貌似没有用到把)
    :return:
    """
    salary = int(input("输入您的工资：\n"))
    keep_going = True
    while keep_going:
        print(product_list)  # todo 我要的效果是分段打印，并非一串打印
        choice = input("请选择货号：\n")
        if choice in product_info:
            a = product_info[choice]['货名']
            b = user_info[user_name]['购物车']
            print(a)
            b.append(a)
            c = input("还继续购物吗？按q退出，或任意键继续：\n")
            if c == "q":
                keep_going = False
            else:
                continue
        elif len(choice) == 0 or choice not in product_info:
            print('您输入的有误，请重新输入')
            c = input("还继续购物吗？按q退出，或任意键继续：\n")
            if  c =="q":
                keep_going = False
            else:
                continue
        print(b)  # todo 033



    pass  # 购买商品前，先打印商品列表

def main():
    """
    # 以下是程序开始的地方
    :return:
    """
    user_name = input("用户名：\n")
    if loggin(user_name) == False:
        continue
    if loggin(user_name) == user_name:

        while True:
            goodslist = PrettyTable(["ID", "功能菜单"])
            goodslist.align["功能菜单"] = "r"  # l 左对齐 r右对齐，默认居中
            goodslist.padding_width = 2  # 填充的宽度 [左右两边的像素]
            goodslist.add_row(["1", "查询商品列表"])
            goodslist.add_row(["2", "查询购物车"])
            goodslist.add_row(["3", "开始购物"])
            goodslist.add_row(["4", "退出"])
            print(goodslist)

            menu_dic = {
                '1': print_product_list,
                '2': fetch,
                '3': buy,
                '4': exit
            }
            while True:
                choice = input('>>>选择操作项目：').strip()
                if len(choice) == 0 or choice not in menu_dic:
                    continue
                elif choice == '4':
                    break
                else:
                    menu_dic[choice](user_name)
            """
            此处判断浪费了很多代码，想想怎么优化一下
        """



if __name__ == "__main__":
    main()

# input().strip() 搭配
# 你这样写可以，但是给人感觉不高大上
