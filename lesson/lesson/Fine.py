#!/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "Gao"

purple_red_str = '\033[35;1m'
red_str = '\033[31;1m'
green_str = '\033[32;1m'
purple_str = '\033[34;1m'

str_end = '\033[0m'

# 定义一个简单的管理员用户名和密码
admin_name = 'admin'
admin_passwd = 'admin'

# 这个变量用来展示给管理员，并且让其选择管理入口
admin_menu ='''以下是管理员选项：
按1：创建讲师；
按2：创建班级；
按3：创建课程
：>>>'''

import pickle
import time


class School(object):

    school_brand = 'Oldboy'

    def school_info(self, name, address, city, *args):
        '''
        这是定义一个学校的基本信息的方法，由school_info的字典记录信息
        :param name: 学校的名称
        :param address: 学校的地址
        :param city: 学校所在的城市
        :param args: 学校的其他信息
        :return: school_info
        '''
        school_info = {}
        school_info['School_Name'] = name
        school_info['School_Address'] = address
        school_info['School_City'] = city
        school_info['School_Other'] = args
        school_info['School_Brand'] = self.school_brand
        return school_info

    def course_info(self, name, price, outline, *args):
        '''
        这是定义一个课程的基本信息的方法，由course_info的字典记录信息
        待外界传入信息收录。
        :param name: 课程的名称
        :param price: 课程的价格
        :param outline: 课程的大纲
        :param args: 课程的其他信息
        :return:
        '''
        course_info = {}
        course_info['Course_Name'] = name
        course_info['Course_Price'] = price
        course_info['Course_Outline'] = outline
        course_info['Course_Other'] = args
        return course_info

    def classes_info(self, name, semester, course, date, teacher, *args):
        '''
        这是定义一个班级的基本信息的方法，由classes_info的字典记录信息
        待外界传入信息收录。
        :param name: 班级名称
        :param semester: 班级学期
        :param course: 课程名称
        :param date: 开课时间
        :param teacher: 讲师
        :param args: 班级的其他信息
        :return:
        '''
        classes_info = {}
        classes_info['Classes_Name'] = name
        classes_info['Classes_Semester'] = semester
        classes_info['Classes_Course'] = course
        classes_info['Classes_Date'] = date
        classes_info['Classes_Teacher'] = teacher
        classes_info['Classes_Other'] = args
        return classes_info

class Student(School):
    '''
    定义一个学生的类，继承了学校的类,主要用到学校类里面的course_info,classes_info,school_info
    '''
    def __init__(self, id, name, age, sex):
        self.NAME = name
        self.AGE = age
        self.SEX = sex
        self.ID = id

    def study_record(self, attend_record, sign_record, sign_record_date, mark):
        '''
        定义一个学生的学习记录
        :param attend_record:上课记录
        :param sign_record: 签到记录
        :param sign_record_date: 签到时间
        :param mark: 成绩
        :return:
        '''
        study_record = {}
        study_record['Attend_Record'] = attend_record
        study_record['Sign_Record'] = sign_record
        study_record['Sign_Record_Date'] = sign_record_date
        study_record['Mark'] = mark

class Teacher(School):
    '''
    定义一个讲师的类，继承了学校的类,主要用到学校类里面的course_info,classes_info,school_info
    '''
    def __init__(self, id, name, age, sex):
        self.NAME = name
        self.AGE = age
        self.SEX = sex
        self.ID = id

# print(purple_red_str+'**********下面输入学校信息_school_info**********'+str_end)
# school_info_input_name = input(red_str+'输入学校名称'+str_end).strip()
# school_info_input_address = input(purple_str+'输入学校地址'+str_end).strip()
# school_info_input_city = input(green_str+'输入学校所在地'+str_end).strip()
#
#
# print(purple_red_str+'**********下面输入课程信息_course_info**********'+str_end)
# course_info_input_name = input(red_str+'输入课程名称'+str_end).strip()
# course_info_input_price = input(purple_str+'输入课程价格'+str_end).strip()
# course_info_input_outline = input(green_str+'输入课程大纲'+str_end).strip()
#
#
# print(purple_red_str+'**********下面输入班级信息_classes_info**********'+str_end)
# classes_info_input_name = input(red_str+'输入班级名称'+str_end).strip()
# classes_info_input_semester = input(purple_str+'输入班级学期'+str_end).strip()
# classes_info_input_course = input(purple_red_str+'输入班级课程'+str_end).strip()
# classes_info_input_date = input(green_str+'输入班级开课时间'+str_end).strip()
# classes_info_input_teacher = input(red_str+'输入班级讲师'+str_end).strip()

role_choice = input('请输入您的角色：讲师按1，学员按2，管理员按3').strip()

while True:

    # 如果按1就进入讲师管理模块：
    if role_choice == '1':
        break

    # 如果按2就进入学员管理模块：
    elif role_choice == '2':

        break

    # 如果按3就进入管理员管理模块，但是需要输入密码确认，admin/admin：
    elif role_choice == '3':
        admin_confirm_name = input('请输入管理员用户名:>>').strip()
        admin_confirm_passwd = input('请输入管理员密码：>>').strip()

        if admin_confirm_name == admin_name and admin_confirm_passwd == admin_passwd:

            print(purple_red_str + '**********欢迎进入管理界面**********' + str_end)
            admin_func_choice = input(admin_menu).strip()

            # 开始创建讲师,Teacher类与School类关联
            if admin_func_choice == '1':

                print(purple_red_str + '***下面输入讲师的信息_Teacher_info***' + str_end)
                teacher_id = input(red_str + '输入讲师工号' + str_end).strip()
                teacher_name = input(red_str + '输入讲师姓名' + str_end).strip()
                teacher_sex = input(purple_str + '输入讲师性别' + str_end).strip()
                teacher_age = input(green_str + '输入讲师年龄' + str_end).strip()

                print(purple_red_str + '***下面输入讲师所在学校的信息_Teacher_School_school_info***' + str_end)
                teacher_school_name = input(red_str + '输入所在学校的名称' + str_end).strip()
                teacher_school_addr = input(green_str + '输入所在学校的地址' + str_end).strip()
                teacher_school_city = input(purple_str + '输入所在学校的城市' + str_end).strip()

                # 实例化一个Teacher类，使用析构函数方法
                new_teacher = Teacher(teacher_id,
                                      teacher_name,
                                      teacher_age,
                                      teacher_sex)

                # 返回一个字典数据给新建的讲师数据
                new_teacher_info = {}
                # 将Teacher类的析构函数信息赋值给new_teacher_info的['Info']
                new_teacher_info['Info'] = new_teacher.__dict__
                # 将School类的school_info函数信息赋值给new_teacher_info
                new_teacher_info = new_teacher.school_info(teacher_school_name,
                                                           teacher_school_addr,
                                                           teacher_school_city)


                # 这样就把老师的属性全部创建好，记得pickle到文件
                print(new_teacher_info)

                '''记得返回值用pickle保存到文件，再break'''
                break

            # 开始创建班级,用School类中的classes_info函数
            elif admin_func_choice == '2':

                print(purple_red_str + '***下面输入班级的信息_School_classes_info***' + str_end)
                classes_name = input(red_str + '输入班级名称' + str_end).strip()
                classes_semester = input(red_str + '输入班级学期' + str_end).strip()
                classes_course = input(purple_str + '输入课程名称' + str_end).strip()
                classes_date = input(green_str + '输入开课时间' + str_end).strip()
                classes_teacher = input(red_str + '输入班级负责讲师' + str_end).strip()


                print(purple_red_str + '***下面输入班级所在学校的信息_School_school_info***' + str_end)
                classes_school_name = input(red_str + '输入所在学校的名称' + str_end).strip()
                classes_school_addr = input(green_str + '输入所在学校的地址' + str_end).strip()
                classes_school_city = input(purple_str + '输入所在学校的城市' + str_end).strip()

                # 实例化School类
                new_classes = School()

                new_classes_info = {}
                # 将School类中的school_info的信息传给new_classes_info['School Info']
                new_classes_info['School Info'] = new_classes.school_info(classes_school_name,
                                                                          classes_school_addr,
                                                                          classes_school_city)
                # 将School类中的classes_info的信息传给new_classes_info['Classes Info']
                new_classes_info['Classes Info'] = new_classes.classes_info(classes_name,
                                                                     classes_semester,
                                                                     classes_course,
                                                                     classes_date,
                                                                     classes_teacher)
                # 这样就把班级的属性全部创建好，记得pickle到文件
                print(new_classes_info)

                '''记得返回值用pickle保存到文件，再break'''

                break

            # 开始创建课程,用School类中的course_info函数
            elif admin_func_choice == '3':

                print(purple_red_str + '***下面输入课程的信息_School_course_info***' + str_end)
                course_name = input(red_str + '输入课程名称' + str_end).strip()
                course_price = input(red_str + '输入课程价格' + str_end).strip()
                course_outline = input(purple_str + '输入课程大纲' + str_end).strip()

                print(purple_red_str + '***下面输入课程所在学校的信息_School_school_info***' + str_end)
                course_school_name = input(red_str + '输入所在学校的名称' + str_end).strip()
                course_school_addr = input(green_str + '输入所在学校的地址' + str_end).strip()
                course_school_city = input(purple_str + '输入所在学校的城市' + str_end).strip()

                # 实例化School类
                new_course = School()

                new_course_info = {}
                # 将School类中的school_info的信息传给new_course_info['School Info']
                new_course_info['School Info'] = new_course.school_info(course_school_name,
                                                                        course_school_addr,
                                                                        course_school_city)
                # 将School类中的classes_info的信息传给new_course_info['Course Info']
                new_course_info['Course Info'] = new_course.course_info(course_name,
                                                                         course_price,
                                                                         course_outline)
                # 这样就把课程的属性全部创建好，记得pickle到文件
                print(new_course_info)

                '''记得返回值用pickle保存到文件，再break'''

                break

            else:
                break
        else:
            print('管理员身份验证有误！')
            break
    else:
        break_input = input("您的输入有误，请重新输入，或按B/b退出:>>")
        if break_input == 'B' or break_input == 'b':
            break
        else:continue


