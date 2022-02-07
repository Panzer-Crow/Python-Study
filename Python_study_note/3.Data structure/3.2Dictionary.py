# 作者: Panzer_Crow
# 说明: Python学习笔记
# 用途: 岭协智能化团队——Python学习第一期
# 知识体系参考: 马士兵教育Python基础版杨淑娟老师授课，特别鸣谢
# 课程网址: https://www.bilibili.com/video/BV1wD4y1o7AS
# 注意：本笔记仅用于岭协智能化团队Python学习交流
# 时间: 2022/1/23 18:52

# 13.0字典
# 说明：和列表一样，值是可变序列，且元素可以是任何形式，但不同的是，字典是无序序列
# 区别：字典以键值对存储
# 注意：键是不可变序列，但是值是可以变的
# 特点：1.以key-value对形式存在，键不可重复，重复会显示重复的最后一个值
#     2.元素位置无序
#     3.key是不可变对象，不可用不可变对象作键
#         plus:可变对象：列表；不可变对象：整数，字符串
#     4.动态伸缩，不需要提前分配空间
#     5.会浪费较大内存，其策略是用空间换时间
"""
【定义字典】
scores =  {    '张三': 100,   '李四'  :     98,    '王五':45}
【字典名】 【花括号】    【逗号】 【键】【冒号】【值】
"""

# 13.1字典的原理
# 原理：通过hash（key）函数，根据字典的键（key）查找value的位置


# 13.2字典的创建和删除
'''
【字典的创建】
[方式一：使用花括号]
scores={'张三':100,'李四':98,'王五':45}
[方式二：使用内置函数dict()]（键不加引号，值加不加引号取决于其数据类型）
dict(name='jack',age=20)
'''

# 13.3字典的查询操作
'''
【字典元素的获取】
[方式一：使用方括号[]]
scores['张三']
[方式二：使用方法get()]
scores.get('张三')
'''
######
# scores={'张三':100,'李四':98,'王五':45}
# print(scores['张三'])
# print(scores.get('张三'))
# 区别：如果找不到对应键值，方括号会报错，而方法.get()会返回None
# 特别说明，使用方法.get()时，若指定键不存在也可以使其返回一个你指定的值
# #####示例
# scores={'张三':100,'李四':98,'王五':45}
# print(scores.get('张三',5))    #能找到指定键值，设定值无效
# print(scores.get('其他人',5))   #指定若找不到键值返回5


# 13.4字典元素的增删改操作
'''
【字典的键值判断操作】
[键 in 字典]
[键 not in 字典]
'''
# #####示例（判断'张三'是否在字典中）
# scores={'张三':100,'李四':98,'王五':45}
# print('张三' in scores)
'''
【字典元素的删除】
del scores['待删除元素的键']  #删除字典一部分元素
scores.clear()             #请空字典
'''
# #####示例（删除某些元素）
# scores={'张三':100,'李四':98,'王五':45}
# del scores['张三']
# print(scores)
# #####示例（清空整个字典）
# scores={'张三':100,'李四':98,'王五':45}
# scores.clear()
# print(scores)
'''
【字典元素的新增】
字典名['新增元素键']=新增元素值
'''
######
# scores={'张三':100,'李四':98,'王五':45}
# scores['hsx']=100000
# print(scores)
'''
【字典元素的修改】（与元素新增格式相似）
字典名['待修改元素键']=待修改元素改变后的值
'''
# scores={'张三': 100,'李四':98,'王五':45,'hsx':100000}
# scores['hsx']=99999
# print(scores)


# 13.5获取字典视图
'''
【获取字典视图】——使用以下三个方法
[keys()]获取字典中所有的key
[values()]获取字典中所有的value
[items()]获取字典中所有的key,value对
'''
# #####示例：
# scores={'张三':100,'李四':98,'王五':45}
# keys=list(scores.keys())
# print(keys)       #并将其转换为列表形式
# values=list(scores.values())
# print(values)   #并将其转换为列表形式
# items=scores.items()
# print(items)
# print(list(items))  #实际上此列表的元素为元组


# 13.6字典的遍历
'''
【字典的遍历】
for item in scores:
    print(item)
说明：获取的item是字典元素的键
'''
######
# scores={'张三':100,'李四':98,'王五':45}
# for item in scores:
#     print(item,scores[item],scores.get(item))  #分别使用方括号和方法来取得元素的值


# 13.7字典推导式
'''
【字典生成式】
[使用内置函数zip()]
#items和value是列表，属于可迭代对象
{item.upper(): value  for item,value in zip(items,value)}
'''
######
# items=['h','s','x']
# values=[1,2,3]
# scores={item.upper():value  for item,value in zip(items,values)} #此处的upper是使键大写的
# print(scores)
