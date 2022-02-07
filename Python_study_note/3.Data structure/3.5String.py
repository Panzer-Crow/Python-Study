# 作者: Panzer_Crow
# 说明: Python学习笔记
# 用途: 岭协智能化团队——Python学习第一期
# 知识体系参考: 马士兵教育Python基础版杨淑娟老师授课，特别鸣谢
# 课程网址: https://www.bilibili.com/video/BV1wD4y1o7AS
# 注意：本笔记仅用于岭协智能化团队Python学习交流
# 时间: 2022/1/23 18:58


# 16.1字符串创建和驻留
"""
驻留机制：仅保存一份相同且不可变的字符串，后续创建相同字符串不开辟新空间
表现为：两次定义相同字符串，内存地址一直
说明：驻留机制可以避免频繁地创建和销毁对象，提升效率，节约内存，在使用拼接时优先使用
     str类join方法，效率更高
驻留机制几种情况：
①字符串长度为1或0时：只要内容相同，有驻留机制（地址一致）
②符合标识符的字符串（数字+字母+下划线，数字不在开头）：有驻留机制
③字符串只在编译时驻留（python是解释型语言，没有编译，这里的编译理解为运行前的预操作），运行时不会
④在[-5，256]之间的整数数字：有驻留机制
⑤可通过sys中的intern方法强制使两个字符串指向同一个对象
如下：
import sys
s1=sys.intern(s2)
"""
# #####以下实验在python解释器中命令行交互运行，不在pycharm中运行（按win+R）
# #####因为pycharm会优化字符串，使原本没有驻留机制的情况也内存地址相等
# #####情况①
# s1='$'
# s2='$'
# s1 is s2
# #####情况②
# s1='abc%'
# s2='abc%'
# s1=s2
# s3='abcd'
# s4='abcd'
# s3=s4
# #####情况③
# a='abc'
# b='ab'+'c'
# c=''.join(['ab','c'])
# a is b
# b is c
# #####情况④
# a='-5'
# b='-6'
# a is b
# c='-6'
# d='-6'
# c is d
# #####情况⑤
# import sys
# a='abc%'
# b='abc%'
# a is b
# a=sys.intern(b)
# a is b


# 16.2字符串查询
'''
【字符串查询】
[方法index()]查找指定字符串第一次出现位置（索引），找不到报异常
[方法rindex()]查找指定字符串最后一次出现位置（索引），找不到报异常
[方法find()]查找指定字符串第一次出现位置（索引），找不到返回-1
[方法rfind()]查找指定字符串最后一次出现位置（索引），找不到返回-1
'''
######
# s='python..python'
# print(s.index('py'))
# print(s.rindex('py'))
# print(s.find('py'))
# print(s.rfind('py'))


# 16.3字符串大小写转换
# 说明：会产生新的字符串对象
'''
【字符串大小写转换】
[方法upper()]所有字符变大写
[方法lower()]所有字符变小写
[方法swapcase()]所有大写变小写，所有小写变大写
[方法capitalize()]第一个字符大写，其余小写
[方法title()]，每个单词第一个字符大写，其余小写
'''
######
# s='PyThOn,HeLlO WlOrD'
# s1=s.upper()
# print(s1)
# s2=s.lower()
# print(s2)
# s3=s.swapcase()
# print(s3)
# s4=s.capitalize()
# print(s4)
# s5=s.title()
# print(s5)


# 16.4字符串内容对齐
'''
【字符串对齐】
[方法center(宽度,填充符（默认空格）)]居中对齐
[方法ljust(宽度,填充符（默认空格）)]左对齐，宽度小于实际宽度返回原字符串
[方法rjust(宽度,填充符（默认空格）)]右对齐，宽度小于实际宽度返回原字符串
[方法zfill(宽度)]右对齐，只接受一个参数，左边用0填充，宽度小于实际宽度返回原字符串
'''
######
# s='python'
# print(s.center(8,))
# print(s.center(8,'*'))
# print(s.center(5))
# print('-----------')
# print(s.ljust(8,))
# print(s.ljust(8,'*'))
# print(s.ljust(5))
# print('-----------')
# print(s.rjust(8,))
# print(s.rjust(8,'*'))
# print(s.rjust(5))
# print('-----------')
# print(s.zfill(8))


# 16.5字符串劈分
'''
【字符串劈分】
说明：返回值为列表[]
[方法split(sep=分割符,maxsplit=最大分割次数)]左劈分，sep参数指定分割符（默认为空格），maxsplit指定最大劈分次数
[方法rsplit(sep=分割符,maxsplit=最大分割次数)]右劈分，sep参数指定分割符（默认为空格），maxsplit指定最大劈分次数
'''
######
# s1='hello world python'
# s2='hello*world*python'
# print(s1.split())
# print(s1.split(sep=' '))
# print(s1.split(sep=' ',maxsplit=1))
# print(s2.split(sep='*'))
# print('-----------------')
# print(s1.rsplit())
# print(s1.rsplit(sep=' '))
# print(s1.rsplit(sep=' ',maxsplit=1))
# print(s2.rsplit(sep='*'))


# 16.6字符串判断
'''
【字符串判断操作】
[方法isidentifier()]：是否为合法标识符
[方法isspace()]：是否全由空白字符（回车，换行，水平制表符）组成
[方法isalpha()]：是否全由字母组成
[方法isdecimal()]：是否全由十进制数组成
[方法isnumeric()]：是否全由数字组成（罗马数字也算）
[方法isalnum()]：是否全由数字和字母组成
'''
######
# print('!qwe'.isidentifier())
# print('  \n'.isspace())
# print('adc'.isalpha())
# print('1023'.isdecimal())
# print('12Ⅰ②'.isnumeric())
# print('a2'.isalnum())


# 16.7字符串替换与合并
'''
【字符串替换】
[方法replace(被指定替换字符子串,用于替换的字符字串,最大替换次数（可不写，默认为最大）)]字符串替换
[方法:'用于分隔字符'.join(含有字符串对象（元组/列表/字符串）)]将列表/元组中的字符串合并成一个字符串
'''
######
# s='hello,python,python,python'
# print(s)
# print(s.replace('python','java',))
# print(s.replace('python','java',2))
# print('----------------')
# lst=['hello','python','java']
# print(lst)
# print('|'.join(lst))


# 16.8字符串比较
'''
【字符串比较操作】
使用的运算符：>,>=,<,<=,==,!=
说明：比较两个字符串的第一个字符，相等则比较下一个字符；比较的是其原始值，可调用ord函数得到
    ord函数的对应的是chr函数，输入原始值可得到对应字符
'''
######
# print('apple'>'app')
# print('apple'>'banana')
# print(ord('a'))
# print(ord('b'))
# print(chr(97))
# print(chr(98))


# 16.9字符串切片
'''
说明：字符串是不可变类型，切片将产生新的对象
字符串名[start:end:step]    （不包含end）
'''
######
# s='python,hello'
# print(s[:6])
# print(s[::-1])


# 16.10字符串格式化字符串
'''
说明：格式化字符串——按一定格式输出字符串
【格式化字符串】
[%  作占位符]   '字符串...%s...%d...'  %  (替换变量表)
 %宽度.精度f
[{} 作占位符]   ’字符串...{0}...{1}...'.format(替换变量表)
[f-string形式]  f'字符串{变量名1}....{变量名2}'
'''
# name='hsx'
# weapon='sword'
# print('That is %s with his %s' % (name,weapon))
# print('That is {0} with his {1}'.format(name,weapon))
# print(f'That is {name} with his {weapon}')


# 16.11字符串编码与解码
'''
【字符串解码与编码】
编码：使用.encode(encoding='编码格式')方法
    encoding='GBK'    #一个中文占两个字节
    encoding='UTF-8'  #一个中文占三个字节
解码：使用byte.decode.(encoding='编码格式')
'''
# #####编码
# s='你好'
# print(s.encode(encoding='GBK'))
# #####解码
# byte=b'\xc4\xe3\xba\xc3'
# print(byte.decode(encoding='GBK'))
