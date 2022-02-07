# 作者: Panzer_Crow
# 说明: Python学习笔记
# 用途: 岭协智能化团队——Python学习第一期
# 知识体系参考: 马士兵教育Python基础版杨淑娟老师授课，特别鸣谢
# 课程网址: https://www.bilibili.com/video/BV1wD4y1o7AS
# 注意：本笔记仅用于岭协智能化团队Python学习交流
# 时间: 2022/1/23 18:54


# 14.0元组
# 说明：元组为不可变序列，没有增删改操作，没有生成式
"""
可变序列（对其作操作后，内存地址没有发生更改）：列表，字典
不可变序列（做操作后内存地址会发生更改，产生了新的数据结构）：字符串，元组
"""
'''
【格式】
t=('Python','hello','90')
说明：储存元素和列表相似，但和列表不同：列表用[]定义，元组用()定义
'''

# 14.1元组创建方式
'''
【元组创建方式】
[使用小括号]
t=('Python','hello',90)
[使用内置函数]
t=tuple(('Python','hello',90))
[创建只包含一个元组的元素需使用逗号和小括号，不加逗号会认为它是其本来的数据类型]
t=(10,)
'''
# #####示例
# t1=('Python','hello',90)
# t2='Python','hello',90    #可以省略括号不写
# t3=tuple(('Python','hello',90))
# t4=(10,)
# print(type(t1),t1)
# print(type(t2),t2)
# print(type(t3),t3)
# print(type(t4),t4)
# #####创建空元组
# t4=()
# t5=tuple()


# 14.2将元组设计为不可变序列的原因
# 原因：多任务环境下，同时操作类型不需要加锁
# 注意：不允许修改元组元素的引用（对应位置是什么元素在元组写好后不可修改）
#     但是可以对元组中元素是可变对象的数据做修改
######
# t=(10,[1,2],20)
# print(t)
# print(t[0])
# print(t[1])
# print(t[2])
# t[1].append(3)   #元组中元素为可变序列，可对其数据做修改（内存地址不变）
# print(t)
# print(t[2])


# 14.3元组的遍历
'''
【元组的遍历】
[不知道索引个数，使用遍历]
t=tuple(('Python','hello',90))
for item in t:
    print(item)
[知道索引使用也可以使用索引]
t=tuple(('Python','hello',90))
for i in rand(3):
    print(t[i])
'''
# #####遍历
# t=tuple(('Python','hello',90))
# for item in t:
#     print(item)
# #####索引
# for i in range(3):
#     print(t[i])
