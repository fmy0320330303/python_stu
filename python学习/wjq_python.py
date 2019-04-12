#！/bin/python
#-*- coding:utf-8 -*-
#运算符
#算术运算符
#+，-，*，/，//整除，%求余
# a=3/2
# print(a)
#print(3+4)
#比较运算符
#>,<,=,!=,<=,>=,==
#逻辑运算符
#与（and）  或（or）  非（not）
#赋值运算符
# +=（加），-=（减），*=（乘），/=（除），//=（整除），%=（求余）
# a=3，a=a+1和a += 1是一样的
# a *= 2*3
# print(a)
#成员预算符
#in      not  in
#判断语句
# a=input('提示')
# a=int(a)
# if a > 80 and a<=100:
# 	print('优秀')#默认条件为真
# elif  a>70 and a<=80:
# 	print('良好')
# else:
# 	print('垃圾')
# a=input('提示')
# if a.startswith('a') and a.endswith('c'):
# 	print('hello')
# else:
# 	print(123)
#嵌套判断
# a=input('输入')
# if a.startswith('a'):
# 	if a.endswith('c'):
# 		print('hello world')
# 	else:
# 		print('hello')
# elif a[0] != 'a' and a.endswith('c'):
# 	print('world')
#循环语句
# b=0
# a=(1,2,3,4)
# for i in a:
#      i=int(i)
#      b=b+i
# print(b)
# b=0
# for i in range(1,101,3):
#  	b=b+i
# print(b)
# b=0
# c=0
# for i in range(1,100,2):
# 	b+=i
# print(b)
# for j in range(2,99,2):
# 	c+=j
# print(c)
# d=b-c
# print(d)
# b=0
# c=0
# for i in range(1,100):
# 	if i%2!=0:
# 		b=b+i
# 		print(b)
# 	if i%2==0:
# 		c=c+i
# d=b-c
# print(d)
# a=['abc','Abc','sad','ade','Aded']
# # for i in a:
# # 	if (i.startswith('a') or i.startswith('A')) and i.endswith('c'):
# # 		print(i)
# import random
# a= random .randint(1,2)#从1-2随机选中一个数赋值给a
# print(a)
# a=('a','b','c','d')
# f=list(a)
# f.append("qwe")
# #f=a[0]
# c=tuple(f)
# print(c)
# a=['a','v','d']
# b=a[1]
# print(b)
# 整数（int）
# 浮点数（float）
# 空值（None）
# 布尔值（bool）
# True(真) False(假)
# 字符串（str）
# #3.数据类型
# #bc=12
# #abc = None
# #print(type(12))
# #print(abc)
# #字符串
#查看其数据类型
# #abc="123"+'1'
# #print(type('abc'))
# # abc=123+1
# # print(type(abc))
# 索引
# abc='wdw def   ():'
# print(abc[-0])
#切片用法
# abc='qwer'
#print(abc[1:8:3])
# 将字符串小写变大写
# abc='qwere'
# f=abc.upper()
# print(abc)
#print(abc.upper())
# 首位变大写
# abc='qwert'
# f=abc.capitalize()
# # print(f)
# 查看该元素有多少个
# abc='qwewqre'
# f=abc.count('e')
# print(f)
# 查看该元素的下标号
# abc='wkjdewmdq'
# f=abc.index('q')
# print(f)
# 替换（kk替换p，替换掉前两个p）
# ab='qwperptyup'
# f=ab.replace('p','kk',2)
# print(f)
#判断是否已什么开头
# ab='qwperptyup'
# f=ab.startswith('qw')
#填充
# print(f)
# ab='1oi%s=dd%s'
# f=ab % ('5','2ac')
#去除空格
# ab=' dwd jw '
# f=ab.strip()
# print(f)
#字符串变成列表
# ab='ddjldpdfmnv'
# f=ab.split('p')
# print(f)
# #f=len(ab)
# # print(len(f))
# 内置函数1：type：格式：（type(变量名)）：查看数据类型
# 内置函数 2：len：格式：（len(变量名)）:统计变量有多少个元素
#列表（list）
# abc=['qw',12,[3],22,33,11,44]
# print(abc[::2])
# print(type(abc))
# print(abc[2])
# print(abc[2][0])
#添加一个元素
# abc.append(55)
# print(abc)
#添加任意一个元素
# abc=[22,11,44,33,55]
# abc.insert(-1,8888)
# print(abc)
#删除某一个元素
# abc=[22,11,44,33,55]
#abc.remove(22)
#print(abc)
# abc.pop(2)
# print(abc)
#排序（升序）
#ab=['qw','11','77','33','9','ab','A']
# ab.sort()
# print(ab)
#反转
#ab.reverse()
#print(ab)
#倒序
# ab.sort()
# ab.reverse()
# print(ab)
#统计某个元素的个数
# ab=['a','b','ca',2,1,'a']
# f=ab.count('a')
# print(f)
#获取元素的下标号
# f=ab.index(1)
# print(f)
#更新
# a=[1,2,34,4]
# b=['a','c','dd','a1']
# a.extend(b)
# print(a)
#复制
# import copy
#
# a=[1,[2,3],3,'a','d',]
# b=copy.deepcopy(a)
# a[1].append(100)
#print(b)
#元组
#统计元组某个元素的个数
# ab=(12,'we','dd2',12)
# f=ab.count(12)
# print(f)
#获取元组元素的下标号
# f=ab.index(12)
# print(f)
#字典
#ab={'name':['小明','小李'],'age':'19','sex':'男'}

#f=ab.index('小明')
# print(ab['age'][0:])
#print(f)
#向字典中添加
# ab={}
# ab['qwe']=123
# ab['age']=22
# print(ab)
#删除
#f=ab.pop('sex')#保存
#ab.popitem()#不保存
#print(ab)
#print(f)
#获取所有的键或者所有的值,所有的键值对
#ab={'name':['小明','小李'],'age':'19','sex':'男'}
#print(ab.key())
# print(ab.values())
# print(ab.items())
#更新
#a='diw'
# b='wdw'
# c=a+b
# print(c)
# a=[1,1,2,3,3,4,3,1]
# b=[]
# for i in range(len(a)):
#     if a[i] not in b:
#         b.append(a[i])
#         print(b)
#文件操作
#在当前目录下对文件的操作a=open('b.txt','w',encoding='utf-8')
#a=open(r'c:\Users\fang\Desktop\a.txt','w',encoding='utf-8')#在桌面的文件操作
#a.write('abc\ndkdk\ndijd')
# print(a.reads())#读取的字符串
# print(a.readlines())#读取的列表
# print(a.readline())#本身有迭代的功能
# print(a.readline())
#批量操作
#写入十行内容
#a=open(r'c:\Users\fang\Desktop\a.txt','r+',encoding='utf-8')
# for i in range(10):#写
#     if i!=9:
#         a.write('{}\n'.format('abc'))
#     else:
#         a.write('{}\n'.format(i))
# a.close()
# a.write('qwert')
# a.close()
# print(a.read())
# a=open(r'kai.jpg','rb')#一般用于存储图片
# a1=a.read()
# print(a1)
# b=open(r'zz.jpg','wb')
# b.write(a1)
# b.close()
#在文件写如九九乘法表
# a=open(r'c:\Users\fang\Desktop\a.txt','w',encoding='utf-8')
#
# for i in range(1,10):
#         for j in range(1,i+1):
#             a.write('{}*{}={}\t'.format(i,j,i*j))
#         a.write('\n')
# a.close()
#函数
#定义函数九九乘法表
# def k():#函数名
#     for i in range(1, 10):
#      for j in range(1,i+1):
#          print('{}*{}={}\t'.format(i,j,i*j),end='')
#      print()
#调用函数
#k()#函数
#结果赋值
# def abc():
#     b=sum(range(101))
#     print(b)
#     print(1010)
#     return b
# print(abc()+10)
#对文件的操作
# a=open(r'c:\Users\fang\Desktop\a.txt','r',encoding='utf-8')
# a1=a.read()
# a1=a1.split('\n')
# a.close()
# for i in a1:
#     if '#' in i:
#         a1.remove(i)
#     elif i =='':
#         a1.remove(i)
# print(len(a1))
# print(a1)
# a=open(r'C:\Users\fang\Desktop\a.txt','r',encoding='utf-8')
# a1=a.readlines()
# a.close()
# for i in a1:
#     if 'abc' in i:
#         print(i)



