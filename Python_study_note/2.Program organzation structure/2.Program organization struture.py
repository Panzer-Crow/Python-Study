# 作者: Panzer_Crow
# 说明: Python学习笔记
# 用途: 岭协智能化团队——Python学习第一期
# 知识体系参考: 马士兵教育Python基础版杨淑娟老师授课，特别鸣谢
# 课程网址: https://www.bilibili.com/video/BV1wD4y1o7AS
# 注意：本笔记仅用于岭协智能化团队Python学习交流
# 时间: 2022/1/23 16:41


# 11.0程序的组织结构
# 说明：同C语言一样，任何算法都可以由顺序结构，选择结构，循环结构构成


# 11.1顺序结构
# 程序调试：【添加断点(点击代码行号后出现红点)】->【选择调试（绿色小虫）】->【在调试器中单步运行】->【在控制台中观察现象】


# 11.2分支结构
#  【预备知识】对象的布尔值
# bool()#函数可用于获取对象的bool值，除以下对象其他对象bool值为True
# bool值为False的对象：
# 【False,数值0，None，空字符串，空列表，空元组，空字典，空集合】
######
# print(bool(False))   #False
# print(bool(None))    #None
# print(bool(0))       #数值0
# print(bool(‘’))      #空字符串
# print(bool([]))      #空列表
# print(bool(list()))  #空列表
# print(bool(()))     #空元组
# print(bool(tuple())) #空元组
# print(bool({}))      #空字典
# print(bool(dict()))  #空字典
# print(bool(set()))   #空集合


"""
【单分支结构】
[if 条件表达式:
    条件执行体]
"""
# #####示例
# money=1000#有1000余额
# s=int(input('请输入取款金额'))#取款金额 #返回值类型为str，需要转化为整形int
# if money>=s: #判断余额是否充足
#    money-=s
#    print('取款成功,余额为：',money)
'''
  【双分枝结构】
[if 条件表达式:
    条件执行体1
 else:
    条件执行体2
# ]
'''
# #####示例(录入整数，让计算机判断为奇数还是偶数)
# num=int(input('输入一个整数'))
# if num%2==0:#为整数
#    print('偶数')
# else:
#    print('奇数')
'''
  【多分支问题】
[
 if 条件表达式1:
     条件执行体1
 elif 条件表达式2:
     条件执行体2
     ...
 else:    #可写可不写，可以省略
     条件执行体n+1
]
'''
# #####示例（键盘录入整数范围，0-100分为A,B,C,D,E,非法输入）
# score=int(input('请输入一个分数'))
# if score>=90 and score <=100:#也可写为【#if 90<= score <=100:】
#    print('A')
# elif score>=80 and score <90:
#    print('B')
# elif score>=70 and score <80:
#    print('C')
# elif score>=60 and score <70:
#    print('D')
# elif score>=0 and score <60:
#    print('E')
# else:
#    print('非法输入')
'''
  【if嵌套】无需过多解释，与C语言相似，记得缩进
'''

# 11.3条件表达式
# 说明：是分支结构的简化，判断条件为True，把x结果赋给变量，为False，把y赋给变量
'''
[x if 判断条件 else  y]
'''
# #####示例
# num_a=int(input('输入整数a'))
# num_b=int(input('输入整数b'))
# print((str(num_a)+'大于等于'+str(num_b))if(num_a>=num_b)else(str(num_b)+'大于等于'+str(num_a)))


# 11.4 pass语句
# 说明：什么都不做，只是一个占位符，用于语法上需要语句的地方先搭建语法结构，使语法上不报错
# #####示例
# answer=int(input('输入'))
# if answer >0:
#    pass
# else:
#    pass


# 11.5循环结构——range()函数【也是一个内置函数】
# 为什么作为循环先导知识：用range()函数产生循环便利的对象
# 说明：用于生成一个整数序列
# 返回值：迭代器对象，看不到具体数据，要看具体数据用list()函数查看整数序列
# 注意：序列包括头但不包括尾，即序列有start,没有stop
# 特点：所占内存空间都相同，不随序列长度发生变化，因为只需要存储start，stop，step
'''
创建range()函数的三种方式
range(stop)            #创建一个[0，stop]的整数序列，步长为1
range(start，stop)      #创建一个[start，stop]的整数序列，步长为1
range(start,stop,step)  #创建一个[start，stop]的整数序列，步长为step
'''
######
# s=range(1,10,1)
# print(s)#s为迭代器对象
# print(list(s))

# 11.6循环结构——while循环
# 说明：判断n+1次，执行n次
'''
while 条件表达式：
      条件循环体
'''
# #####简单示例
# a=1          #初始化变量
# while a<10:  #条件判断
#    print(a) #条件执行体
#    a+=1     #改变变量
# #####示例（计算1-100之间的偶数的和）
# sum=0
# a=1
# while a<=100:
#    if a%2==0 :
#        sum+=a
#    a+=1
# print(sum)


# 11.7循环结构——for-in循环
# 说明：从可迭代对象中依次取出一个值，赋给自定义变量，称为
# 可迭代对象：字符串，序列
# 自定义变量：其实相当于一个形参（可参考C语言）
'''
for 自定义变量 in 可迭代对象：
     循环体
'''
# #####示例（依次取出字符串中字符并打印）
# for item in 'python':
#    print(item)
# #####示例（从序列中依次取出数字并打印）
# for i in range(1,10,1):
#    print(i)
'''
特殊的：如果在循环体中用不到自定义变量，可以用'_'代替
for _ in 可迭代对象:
      循环体
'''
# #####示例
# for _ in range(1,10,1):
#    print('人生苦短，我用Python')
# #####示例（计算1-100之间的偶数）
# sum=0
# for i in range(1,101,1):
#    if i%2==0:
#        sum+=i
# print(sum)
# ####示例
# 要求：输出100-999间的水仙花数（水仙花数：个位数子**3+十位数**3+百位数**3==原来数字）
# for i in range(100,1000,1):
#    ge=i%10        #个位数子
#    shi=(i//10)%10 #十位数字
#    bai=i//100     #百位数字
#    if (ge ** 3 + shi ** 3 + bai ** 3) == i:
#        print(i)


# 11.8循环结构——break,continue,else语句
'''
【流程控制语句break】
说明：用于结束循环，与分支结构if或循环while一起使用
'''
# #####示例（从键盘录入密码，最多录入3次，正确就结束循环）
# for i in range(3):
#    pwd=input('请输入密码')
#    if pwd=='8888':
#        print('密码正确')
#        break
#    else:
#        print('密码错误')
'''
【流程控制语句continue】
说明：用于结束当前循环，进行下一次循环，需要区分break；
break用于直接跳出循环（结束循环），而continue只是跳出本次循环，下一次继续
'''
# #####示例（要求输出1-50之间所有的5的倍数， 且要求使用continue）
# for i in range(1,51,1):
#    if i%5!=0:
#        continue
#    print(i)
'''
【else语句的用法】
[与if搭配]条件不成立时执行else

[与while搭配]没有碰到break执行else
[与for搭配]没有碰到break执行else
说明：循环正常执行的次数执行完就会执行else
'''
# #####示例（输密码，加一个三次输入后的提示语）
# text='8888'
# for i in range(3):
#    a=input('请输入密码')
#    if a==text:
#        print('密码正确')
#        break
#    else:
#        print('密码错误')
# else:
#    print('已输入三次密码，停止输入')
# #####示例（同上，用while和else）
# a=0                       #初始化变量
# while a<3:                #if条件表达式语句
#    psw=input('请输入密码')  #条件执行体
#    if psw=='8888':
#        print('密码正确')
#        break
#    else:
#         print('密码错误')
#    a+=1                   #计数值+1
# else:
#     print('已输入三次密码，停止输入')
'''
注意：二层循环中的break和continue只作用于本层循环
'''
