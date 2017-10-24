#!/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "Gao"

"""
学员member_summary=[]
老师teacher_summary=[]
课程course_summary=[]

学员_info，学号={"学号"：'', '姓名':'','注册'：0/1，'课程'：{'学校'：'', '班级'：''，'讲师'：''}}
讲师_info，工号={"工号"：'', '姓名':'','课程'：{'学校'：'', '班级'：''，'讲师'：''}}

"""


class School(object):

    def __init__(self):
        '''
        self.COURSE_NAME  # 课程名称
        self.COURSE_CYCLE  # 课程周期
        self.COURSE_PRICE  # 课程价格
        self.COURSE_PRICE_DISCOUNT  # 课程折扣，默认是100%（没有折扣）
        self.COURSE_LOCATION  # 课程地点
        '''
        self.COURSE_LIST = ['Linux', 'Python', 'Go']
        self.COURSE_NAME = None
        self.COURSE_CYCLE = None
        self.COURSE_PRICE = None
        self.COURSE_PRICE_DISCOUNT = 1
        self.COURSE_LOCATION = None
        self.CLASSROOM = None
        self.TEACHER = None



    def course(self):
         '''
         定义开课的方法，用来创建对应的课程地点。
         Linux和Python在北京，Go在上海
         :return:
         '''
         choice = input("请输入课程名>>:(Linux, Python, Go)").strip()
         course_info ={}

         def create_course():
             '''
             为了创建课程info的对应关系而减少代码，没卵用
             :return:没有返回值
             '''
             course_info['COURSE_NAME'] = self.COURSE_NAME
             course_info['COURSE_CYCLE'] = self.COURSE_CYCLE
             course_info['COURSE_PRICE'] = self.COURSE_PRICE * self.COURSE_PRICE_DISCOUNT
             course_info['COURSE_LOCATION'] = self.COURSE_LOCATION

         while True:
             if choice in self.COURSE_LIST:
                 if choice =='Linux':
                     self.COURSE_NAME = choice
                     self.COURSE_CYCLE = '40weeks'
                     self.COURSE_PRICE = 12000
                     self.COURSE_PRICE_DISCOUNT = 1
                     self.COURSE_LOCATION = 'Beijing'
                     create_course()

                     return course_info

                 elif choice =='Python':
                     self.COURSE_NAME = choice
                     self.COURSE_CYCLE = '60weeks'
                     self.COURSE_PRICE = 15000
                     self.COURSE_PRICE_DISCOUNT = 1
                     self.COURSE_LOCATION = 'Beijing'
                     create_course()

                     return course_info

                 elif choice == 'Go':
                     self.COURSE_NAME = choice
                     self.COURSE_CYCLE = '80weeks'
                     self.COURSE_PRICE = 20000
                     self.COURSE_PRICE_DISCOUNT = 1
                     self.COURSE_LOCATION = 'Shaghai'
                     create_course()

                     return course_info

             else:
                 print('输入有误，请重新输入！')
                 choice = input("请输入课程名>>:(Linux, Python, Go)(或按B/b退出)").strip()
                 if choice == 'B' or choice == 'b':
                     break
                 else:continue

class Member(School):

    def __init__(self, name, course_name, classroom, enroll=1 ):
        super(School, self).__init__(self)
        self.NAME = name
        self.ENROLL = 1
        self.CLASSROOM = classroom
        self.COURSE_NAME = course_name


member_1 = School()
print(member_1.course())

obj2 = Member('gao','Go','PY01')
print(obj2.__dict__)
