# 作者: Panzer_Crow
# 说明: Python学习笔记
# 用途: 岭协智能化团队——Python学习第一期
# 知识体系参考: 马士兵教育Python基础版杨淑娟老师授课，特别鸣谢
# 课程网址: https://www.bilibili.com/video/BV1wD4y1o7AS
# 注意：本笔记仅用于岭协智能化团队Python学习交流
# 时间: 2022/2/4 17:26

"""
面向对象三大特征：封装，继承，多态
【封装】
    [对于不希望类里的对象被外部访问，在前面使用两个“_”]
        此时一般情况在类外不可调用显示该属性，在类里边可以调用显示
        特殊的，其实也可以通过dir显示后找到对应对象属性，但是为了安全性，不建议这么访问
【继承】
    [Python支持多继承，即从多个父类继承其中的构造函数，没有继承默认继承object]
class 子类类名（父类1，父类2，...）
【多态】详见Xmind说明
"""


# #####封装示例
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#
#     def show(self):
#         print(self.name, self.__age)
#
#
# stu1 = Student('tom', 20)
# stu1.show()


# stu1=Student('tom', 20) #运行会报错

# #####继承示例(Person继承object，Teacher和Student继承Person)
# super()方法用于调用父类中内容
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(self.name, self.age)
#
#
# class Student(Person):
#     def __init__(self, name, age, stu_number):
#         super().__init__(name, age)
#         self.stu_number = stu_number
#
#
# class Teacher(Person):
#     def __init__(self, name, age, teacher_number):
#         super().__init__(name, age)
#         self.teacher_number = teacher_number
#
#
# stu1 = Student('tom', 20, '1001')
# tch1 = Teacher('jack', 30, '1002')
#
# stu1.info()
# tch1.info()
# 说明：info()方法在Student以及Teacher类中未定义，但是继承自父类，可以直接使用
#      初始化中已经有的可以使用super()函数继承

# #####示例：重写__str()__方法用于查看对象描述
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return '名字是{0}，年龄为{1}'.format(self.name, self.age)
#
#
# stu1 = Student('tom', 20)
# print(stu1)  # 默认调用__str()__方法

# #####多态（此例子可展现，Python多态特点，例中去掉父类Animal仍可执行）
# class Animal(object):
#     def eat(self):
#         pass
#
#
# class Dog(object):
#     def eat(self):
#         print('eat fish')
#
#
# class Cat(object):
#     def eat(self):
#         print('eat bone')
#
#
# def fun(obj):
#     obj.eat()
#
#
# def main():
#     fun(Dog())
#     fun(Cat())
#
#
# if __name__ == '__main__':
#     main()

# #####借用课程中的例子说明实例对象传参过程
# class Person(object):
#     def __new__(cls, *args, **kwargs):
#         print("执行__new__,cls的id为{0}".format(id(cls)))
#         obj = super().__new__(cls)
#         print("创建对象的id为{0}".format(id(obj)))
#         return obj
#
#     def __init__(self, name, age):
#         print("调用__init__,self的id为{0}".format(id(self)))
#         self.name = name
#         self.age = age
#
#
# print('object类对象id为{0}'.format(id(object)))
# print('Person类对象的id为{0}'.format(id(Person)))
#
# # 创建Person类对象p1
# p1 = Person('tom', 20)
# print('p1实例对象的id值为{0}'.format(id(p1)))
