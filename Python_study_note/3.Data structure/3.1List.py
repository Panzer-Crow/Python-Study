# 作者: Panzer_Crow
# 说明: Python学习笔记
# 用途: 岭协智能化团队——Python学习第一期
# 知识体系参考: 马士兵教育Python基础版杨淑娟老师授课，特别鸣谢
# 课程网址: https://www.bilibili.com/video/BV1wD4y1o7AS
# 注意：本笔记仅用于岭协智能化团队Python学习交流
# 时间: 2022/1/23 18:48

# 12.0列表
"""
#说明：列表可以用于存储多个元素，其每个元素可以是：字符串，浮点，整型
#理解：实际上列表内部存储的是内部元素的内存地址
#特点：1.列表对象按顺序存储
      2.列表映射唯一一个元素，且从零号元素开始
      3.列表可以存储重复数据
      4.任意数据类型可以进行混存
      5，会根据元素类型和数量动态分配内存
#【列表形式】-如：
lst=['hello',98.7,8]
"""

# 12.1列表的创建和删除
'''
【创建】
#方式一：使用中括号
#方式二：调用内置函数：list()
'''
######
# lst1=['hello',98.7,8]       #使用方括号创建
# lst2=list(['hello',98.7,8]) #使用内置函数list()创建
# print(lst1)
# print(lst1[0])


# 12.2列表的查询操作
'''
【获取列表中指定元素的索引】
使用：index()
说明：如果列表中有多个相同元素，只返回第一个元素的索引
返回值：返回元素的索引（也即是在列表中的元素编号，元素编号从0开始）
       查询元素不存在，返回ValueError,会报错
plus:也可以在指定的start和stop之间查找
【获取列表中单个元素】
说明：给元素的索引，取出对应元素的value
索引分类：正向索引：0-（n-1）
        逆向索引:(-n)-(-1)
'''
# lst=['hello',98.7,'hello','world','hsx']
# print(lst.index('hello'))   #注意此处不是逗号，是点，是引用lst对象的index方法
# print(lst.index('hello',2,3))#在指定的start和stop之间查找
# print(lst[1])
# print(lst[-4])
'''
【元素查询——切片（获取列表中多个元素）】
语法：列表名[start:stop:step]
结果：原列表一部分片段的拷贝,一个新列表
范围[start,stop),左开右闭
step：默认为1
      为正数  
      为负数 默认第一个元素为最后一个元素，第一个为最后一个元素，逆序
'''
######
# lst=['hello',98.7,'hello','world','hsx']
# print(lst)
# print(lst[1:4])       #切片：一定注意，是左闭右开的
# print(lst[1:4:1])
# print(lst[1:4:])      #step:省略默认为1
# print(lst[:4:1])      #start：省略默认为0
# print(lst[1::1])      #stop:省略默认为最后一个（默认数字为n，把从0开始的最后一个元素n-1号元素包括进去）
# print('step为-1,逆序')
# print(lst[5:0:-1])    #不包括索引为0
'''
【判断指定元素在列表中是否存在】
元素 in 列表名
元素 not in 列表名
'''
######
# lst=['hello',98.7,'hello','world','hsx']
# print('hello' in lst)
'''
【列表元素的遍历(依次打印)】
for 迭代变量 in 列表名：
    操作 
'''
# lst=['hello',98.7,'hello','world','hsx']
# for i in lst:
#     print(i)


# 12.2列表的增删改操作
'''
【列表元素的增加(id没有变)】
append()    #在列表的末尾添加一个元素
extend()    #在列表的末尾至少添加一个元素
insert()    #在列表的任意位置添加一个元素
#切片        #在列表任意位置添加至少一个元素（对索引号开始的元素做替换）
'''
# #####append()
# lst=['hello',98.7,'hello','world','hsx']
# print(lst)
# lst.append('more')#列表末尾增加元素
# print(lst)
# #####extend()
# lst=['hello',98.7,'hello','world','hsx']
# lst2=[1,2]
# lst.append(lst2)  #向append添加一个列表，它会将列表整体作为一个元素添加到目标列表末尾
# print(lst)
# lst .extend(lst2) #而extend会向列表末尾一次性添加多个元素
# print (lst)
# #####insert()
# lst=['hello',98.7,'hello','world','hsx']
# print(lst)
# lst.insert(7,'add')  #使用insert()函数会把元素添加到给定索引的位置上，并将原来该位置上元素后移
# print(lst)           #但当索引数字大于原列表最大索引时，再增加索引数字大小也只会在原最大索引元素后一位添加新元素
# print(lst.index('add'))
# #####切片(对其后元素用切片替换)
# lst=['hello',98.7,'hello','world','hsx']
# lst3=[4,'asd']
# lst[1:]=lst3  #对索引号开始的元素做替换
# print(lst)
'''
【列表元素的删除操作】
[remove()]
说明：一次删除一个元素；重复元素只删除一个；元素不存在抛出ValueError
[pop()]
说明：删除一个指定索引位置上的元素；指定索引不存在抛出IndexError;不指定索引，删除列表中最后一个元素
[切片]
说明：一次至少删除一个元素，会产生一个新的列表
[clear()]
说明：清空列表
[del]
说明：删除列表
'''
# #####remove()(删除一个元素，有重复只移除第一个)
# lst=['hello',98.7,'hello','world','hsx']
# lst.remove('hello')
# print(lst)
# #####pop()(删除指定位置一个元素)(不指定参数会删除最后一个元素)
# lst=['hello',98.7,'hello','world','hsx']
# lst.pop(1)
# print(lst)
# #####切片（可一次性删除多个元素）
# lst=['hello',98.7,'hello','world','hsx']
# new_lst=lst[1:3]
# print(lst)
# print(new_lst)
# 若不产生新的列表，可如下操作（用空列表对列表元素替代）
# lst=['hello',98.7,'hello','world','hsx']
# lst[1:3]=[]
# print(lst)
# #####clear;清除列表元素
# lst=['hello',98.7,'hello','world','hsx']
# lst.clear()
# print(lst)
# #####del;将列表对象删除,现象是没有定义，会报错
# lst=['hello',98.7,'hello','world','hsx']
# lst.del
# print(lst)
'''
【列表元素的修改】
[指定一个元素赋新值]
lst[n]=修改的值
[为指定的切片赋新值]

'''
# #####一次修改一个值
# lst=['hello',98.7,'hello','world','hsx']
# lst[2]=100
# print(lst)
# #####对一段切片赋新值
# lst=['hello',98.7,'hello','world','hsx']
# lst[1:3]=[1,2,3]
# print(lst)


# 12.4列表的排序
'''
说明：对列表中的元素进行一个由小到大或由大到小的排序
[调用sort()函数]       升序
                     降序：指定reverse=True  (reverse为关键字)
[调用内置函数sorted()] 也可以通过指定reverse=True，进行降序排列
                     注意：此时生成了新列表
'''
# #####sort()函数
# lst=[20,98,87,56,70]
# print('排序前',lst,id(lst))
# lst.sort()
# print('升序排序',lst,id(lst))
# lst.sort(reverse=True)
# print('降序排列',lst)
# #####sorted()函数
# lst=[20,98,87,56,70]
# lst_new=sorted(lst)     #会生成新列表
# print(lst_new)
# lst_new=sorted(lst,reverse=True)
# print(lst_new)


# 12.5列表生成式
'''
说明：生成列表的公式
【语法格式】
   [i for i in  range(1,10)]   #表示产生一个关于表达式为i的从1到9的整数序列
   第一个i是列表元素的表达式
注意：可以产生的表达式只能是有规律的
'''
# #####示例
# lst=[i*i for i in range(1,10)]  #产生关于表达式i*的列表
# print(lst)
