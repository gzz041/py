#!/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "Gao"

class School(object):
    """
    这个类是创建学校，并且在这个类中，要创建课程course，
    课程包含：“课程名称name,周期Cycle,价格Price”
    """
    def __init__(self):
        self.COURSE_NAME = None
        self.COURSE_CYCLE = None
        self.COURSE_PRICE = None
        self.COURSE_LOCATION = None
        self.CLASSROOM = None

    def course(self):
            '''
            定义开课的方法，用来创建对应的课程地点。
            Linux和Python在北京，Go在上海
            :return:
            '''
            choice = input("请输入课程名>>:(Linux, Python, Go)").strip()
            # print(type(choice),choice)
            if choice =='Linux':
                self.COURSE_NAME = choice
                self.COURSE_CYCLE = '40weeks'
                self.COURSE_PRICE = 12000
                self.COURSE_LOCATION = 'Beijing'
                # return self.__dict__

            elif choice =='Python':
                self.COURSE_NAME = choice
                self.COURSE_CYCLE = '60weeks'
                self.COURSE_PRICE = 15000
                self.COURSE_LOCATION = 'Beijing'


            elif choice == 'Go':
                self.COURSE_NAME ==choice
                self.COURSE_CYCLE = '80weeks'
                self.COURSE_PRICE = 20000
                self.COURSE_LOCATION = 'Shaghai'



    def classroom(self, classroom):
        '''
        班级通过学校创建，班级关联课程、讲师
        :param classroom:这个参数需要用户自己输入
        :return: self.CLASSROOM
        '''
        self.CLASSROOM = classroom
        return self.CLASSROOM

class Course(School):
        '''
        这个是课程类，包含课程名称，课程周期，课程价格
        没准已经不用了
        '''
        def __init__(self):
            pass


class Member(School):
    """
    这个是用来创建学员的类，继承了School的父类
    实例化Member后，需要关联学校和班级
    用新式类继承方法
    """
    def __init__(self, name, age, course_name, id):
        super(Member, self).__init__(course_name)
        self.NAME = name
        self.AGE = age
        self.ID = id


class Teacher(School):
    """
    这个是用来创建讲师的类，继承了School的父类
    实例化Teacher后，需要关联学校
    用新式类继承方法
    """
    def __init__(self, name, age, id_num):
        self.NAME = name
        self.AGE = age
        self.ID = id_num

# teacher_name = input("Enter Your Name>>:").strip()
# teacher_course = input("What Course You will Teach{0}>>:".format('Such as Linux Python Go .Choice one')).strip()
# teacher_course_price = input("Enter the Course Price(RMB)>>:").strip()
# teacher_course_cycle = input("Course cycle(How many weeks)>>:").strip()


# teacher = School()
# teacher.course(teacher_course,teacher_course_cycle,teacher_course_price)
# print(teacher.COURSE_CYCLE)
# print(teacher.COURSE_NAME)
# print(teacher.COURSE_PRICE)
#
# teacher.classroom('shanghai')
# print(teacher.CLASSROOM)
# print(teacher.__dict__)


# obj1 = School()
# # obj1.course()
# str_1 = input('输入班级：>>').strip()
# print(obj1.classroom(str_1))


obj1 = School()
res = obj1.course()
print(res)