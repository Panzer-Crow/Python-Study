# 作者: Panzer_Crow
# 说明: Python学习笔记
# 用途: 岭协智能化团队——Python学习第一期
# 知识体系参考: 马士兵教育Python基础版杨淑娟老师授课，特别鸣谢
# 课程网址: https://www.bilibili.com/video/BV1wD4y1o7AS
# 注意：本笔记仅用于岭协智能化团队Python学习交流
# 时间: 2022/1/23 18:56

# 15.0集合
# 说明：属于内置可变类型序列
#     用花括号{}定义（和字典一样）
#     由hash函数计算后确定存放地址，因此和字典一样为无序序列
#     与字典相同，元素不可重复
#     不同的是，其元素不以键值对形式存在，可以理解为没有value的字典
"""
【集合的创建】
[直接{}创建]
s={'python','hello',90}
[内置函数set()创建]
s=set(range(6))
"""
# #####示例
# s1={1,2,3,4,4,5,6,6} #1：直接{}创建
# print('s1=',s1)      #集合不允许重复（有重复会删除）
# s2=set(range(6))     #2：用range()函数创建，set()函数将range()转为集合
# print('s2=',s2)
# s3=set([1,2,3,4,5])  #3.用列表创建，set()函数将列表转换为集合，同时去掉重复元素
# print('s3=',s3)
# s4=set((1,2,3,4,5))  #4：用元组创建，set()函数将元组转换为集合，同时去掉重复元素
# print('s4=',s4)
# s5=set('Python')     #5：用字符串创建，set()函数将字符串转换为集合，同时去掉重复元素
# print('s5=',s5)
# s6=set({1,2,3,4,5})  #6：用集合创建（本条做不做set()操作都是集合），同时去掉重复元素
# print('s6=',s6)
# s7=set()             #创建空集合
# print('s7=',s7)


# 15.1集合的相关操作
'''
【集合元素的判断】
in 或 not in
【集合元素的新增】
[调用add()方法一次新增一个元素]
[调用update()方法一次新增多个元素]
【集合元素的删除】
[remove()方法一次删除指定元素]
[discard()方法一次删除指定元素]
[pop()方法一次删除一个任意元素]
[clear()方法清空集合]

'''
# #####集合元素的判断
# s={10,20,30,40,50,50,60,70,70}
# print(10 in s)
# #####集合元素的新增
# s={10,20,30,40,50,50,60,70,70}
# s.add(80)
# print(s)
# s.update({200,300,400})
# print(s)
# s.update([11,12])  #添加元组
# print(s)
# s.update({13,14})  #添加列表
# print(s)
# #####集合元素的删除
# s={10,20,30,40,50,50,60,70,70}
# s.remove(10)  #指定元素不存在报异常
# print(s)
# s.discard(20) #指定元素不存在不报异常
# print(s)
# s.pop()
# print(s)
# s.clear()
# print(s)


# 15.2集合间的关系
'''
【集合相等（无序：内容相同，集合相等）】
==或!=
【是否为子集】
[调用issubest方法判断]
【是否为超集】
[调用issuperset方法判断]
【是否有交集】
[调用isdisjoint]
'''
######
# s1={1,2,3,4}
# s2={4,3,2,1}
# s3={2,3,4}
# s4={1,2,3,4,5}
# s5={2,3,4,5,6}
# print(s1==s2)           #相等
# print(s3.issubset(s1))  #子集
# print(s4.issuperset(s1))#超集
# print(s5.isdisjoint(s4))#交集：是否没有交集


# 15.3集合的数据操作(操作后原来集合不变)
'''
【取交集】
  [方法intersection()]
  [a & b]
【取并集】
  [方法union()]
  [a | b]
【取差集(A集合-B集合)】
  [方法difference()]
  [a - b]
【对称差集（(A集合和B集合)不交集的部分）】
  [a symmetric_difference]
  [a ^ b](shift+6)
'''
######
# s1={1,2,3}
# s2={2,3,4}
# print(s1.intersection(s2))  #交集
# print(s1&s2)
# print(s1.union(s2))         #并集
# print(s1|s2)
# print(s1.difference(s2))    #差集
# print(s1-s2)
# print(s1.symmetric_difference(s2))  #对称差集
# print(s1^s2)


# 15.4集合生成式
'''
【集合生成式】
s={集合元素表达式 for i in 可迭代对象}
'''
######
# s={i*i for i in range(9)}
# print(s)
