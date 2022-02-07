# 作者: Panzer_Crow
# 说明: Python学习笔记
# 用途: 岭协智能化团队——Python学习第一期
# 知识体系参考: 马士兵教育Python基础版杨淑娟老师授课，特别鸣谢
# 课程网址: https://www.bilibili.com/video/BV1wD4y1o7AS
# 注意：本笔记仅用于岭协智能化团队Python学习交流
# 时间: 2022/1/28 22:39


"""
【异常处理机制 1】
背景：存在例外情况导致产生BUG
如：0不能做除数
解决方式【使用Python的异常处理机制】
使用try-except结构，程序不会报错，会跳过试错部分继续执行
格式：

try:
    判断对错部分程序段
except 判断类型:
    出错时执行语句
后续语句

"""
# #####示例
# try:
#     a=int(input('整数1'))
#     b=int(input('整数2'))
#     result=a/b
#     print(result)
# except ZeroDivisionError:
#     print('除数类型错误')
# print('进程结束')
'''
特殊的：同时检测多种错误
'''
# #####示例
# try:
#     a=int(input('整数1'))
#     b=int(input('整数2'))
#     result=a/b
#     print(result)
# except ZeroDivisionError:
#     print('除数类型错误')
# except ValueError:
#     print('输入类型错误')
# print('进程结束')

'''
【异常处理机制 2】
使用try-except-else结构
格式：

try:
    判断对错部分程序段
except 判断类型:
    出错时执行语句
else:
    没有抛出异常执行语句
后续语句
'''
# #####示例（说明：BaseException可以对所有可能出现的异常情况进行捕获）
# try:
#     a = int(input('输入整数1'))
#     b = int(input('输入整数2'))
#     result = a / b
# except BaseException as e:
#     print('出现错误，抛出异常类型为：', e)
# else:
#     print('进程正常')
#     print('结果为', result)
# print('进程结束')

'''
【异常处理机制 2】
使用try-except-else-finally结构
格式：

try:
    判断对错部分程序段
except 判断类型:
    出错时执行语句
else:
    没有抛出异常执行语句
finally:
    不论程序执行是否抛出错误都会执行的语句
后续语句
'''


"""
【常见异常类型】
ZeroDivisionError  除零
IndexError         序列中没有此引索（index）
KeyError           映射中没有这个键
NameError          未声明/初始化该变量
SyntaxError        Python语法错误
ValueError         传入无效参数
"""

