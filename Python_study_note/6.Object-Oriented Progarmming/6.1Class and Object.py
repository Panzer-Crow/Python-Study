# 作者: Panzer_Crow
# 说明: Python学习笔记
# 用途: 岭协智能化团队——Python学习第一期
# 知识体系参考: 马士兵教育Python基础版杨淑娟老师授课，特别鸣谢
# 课程网址: https://www.bilibili.com/video/BV1wD4y1o7AS
# 注意：本笔记仅用于岭协智能化团队Python学习交流
# 时间: 2022/2/4 14:45


# 注意：在类里面定义的称为方法，在类之外定义的为函数

# 类与对象
"""
【类的组成】类属性，实例方法，静态方法，类方法，初始化方法等
【类的创建】
class 类名 :
    pass
"""


# #####示例（类的创建与对象的创建）
# 类的名称（要求每个单词的首字母大写）
class Student:
    # 类属性（直接写在类里的变量称为类属性）
    native_pace = '吉林'

    # 初始化方法(可以进行赋值操作，将局部变量赋给实例属性)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法
    def eat(self):
        print('实例方法:学生在吃饭')

    # 静态方法（在静态方法中不允许写self）
    @staticmethod
    def method():
        print('定义一个静态方法')

    # 类方法
    @classmethod
    def cm(cls):
        print('类方法')


# 对象的创建（创建的是实例对象：根据类对象创建的就是实例对象）
'''
【（实例）对象的创建】
【格式】
对象名=类名（）
'''
# #####示例
stu1 = Student('Tom', 20)
stu2 = Student('Jack', 21)
# 类属性使用
print(Student.native_pace)
print(stu1.native_pace)
print(stu2.native_pace)
print('--------类方法----------')
# 类方法使用(使用：类名.类方法名)
Student.cm()
print('--------静态方法----------')
# 静态方法使用（）
Student.method()
print('--------动态绑定----------')
# 动态绑定属性（而stu2没有该属性，打印会报错）
stu1.gender = '女'
print(stu1.gender)
# 动态绑定方法（而stu2没有该方法，打印会报错）
def fun():
    print('动态绑定方法')
stu1.fun = fun
stu1.fun()