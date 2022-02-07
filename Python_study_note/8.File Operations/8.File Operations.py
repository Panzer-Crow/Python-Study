# 作者: Panzer_Crow
# 说明: Python学习笔记
# 用途: 岭协智能化团队——Python学习第一期
# 知识体系参考: 马士兵教育Python基础版杨淑娟老师授课，特别鸣谢
# 课程网址: https://www.bilibili.com/video/BV1wD4y1o7AS
# 注意：本笔记仅用于岭协智能化团队Python学习交流
# 时间: 2022/2/6 15:57


"""
【创建/打开文件】
文件对象名（.py文件中创建的） = open(要打开或创建的文件名称,操作模式（默认只读）,编码格式（默认文本文件是GBK）)

"""
# #####open()内置函数创建文件
# 打开或创建文件a.txt并赋给一个文件对象file
# file1 = open('a.txt','r',encoding='GBK')  #与执行的.py文件在同一目录下，可以使用相对路径寻址
# file2=open('b.txt','w')
# file2.write('world')
# print(file1.readlines())
# file1.close()

# #####with语句
# with open('a.txt') as file:
#     print(file.read())

# #####os模块
# import os
# os.system('calc.exe')  # 打开exe文件
# 直接调用可执行文件
# os.startfile('exe文件绝对路径（记得加转义字符\）')

# #####os.walk示例
# import os
# path=os.getcwd()
# lst_file=os.walk(path)
# for dirpath,dirname,filename in lst_file:
#     print(dirpath)
#     print(dirname)
#     print(filename)
#     print('----------------------')

