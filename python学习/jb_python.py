# #！/bin/python
# #-*- coding:utf-8 -*-
#练习》》》》》》》》》》
#质数之和
# a=0
# for i  in range(2,101):
#     for j in range(2,i+1):
#         if i%j==0:
#             break
#     if i==j:
#         a+=i
# print(a)
#求元素最大和第二大的元素
# a=input('输入元素')
# a=list(a)
# b=a.copy()
# b.sort()
# c=[]
# d=[]
# for i in range(len(b)):
#     if b[-1]==b[i] :
#         c.append(b[i])
#     else:
#         d.append(b[i])
# m=[]
# for j in range(len(d)):
#     if d[-1]==d[j]:
#         m.append(d[j])
# l=c+m
# print(l)
#阶乘之和
# a=1
# b=0
# for i in range(1,6):
#      a=a*i
#      b+=a
# print(a)
# print(b)
#去重
# a=input('输入以逗号隔开')
# a.split(',')
# b=[]
# for i in (len(a)):
#     if a[i] not in b:
#         b.append(a[i])
# print(b)
# for i  in range(2,100000,2):
#      a=0
#      for j in range(1,i):
#          if i%j==0 :
#              a=j+a
#      if a==i:
#          print(a)
#try语句的练习应用
# try:
#  a='123'
#  print(a+1)
# except TypeError:\
#  print('hello')
# # else:
#     print('你好')
# if 4>3:
#  raise TypeError('110')
# import day1
# day1.k()
#第一大和第二大的元素
# a=[1,1,1,22,22,3,3]
# b=list(set(a))
# b.sort()
# c=[i for i in a if b[-1]==i or b[-2]==i]
# print(c)
####随机数赋值给变量
# import random
# a=random.randint(1,15)
# for i in range(3):
# 	b = input('数字')
# 	b=int(b)
# 	if a==b:
# 		print('拿钱')
# 		break
# 	if a>b:
# 		print('小了')
# 	if a<b:
# 		print('大了')
# else:
# 		print('赔钱')
# b=input('数字')
# b=b.split(',')
# b=[int(b[0]),int(b[1]),int(b[2])]
# b.sort()
# if b[0]+b[1]>b[2]:
#  if b[0]**2+b[1]**2==b[2]**2:
#   print('直角')
#  elif b[0]**2+b[1]**2>b[2]**2:
#   print('锐角')
#  else:
#   print('钝角')
# def a(x,y):
#     b=[i for i in range(x,y) if (i//100)**3+(i//10%10)**3+(i%10)**3==i]
#     return b
# print(a(100,1000))


# for i in range(100,1000):
#      s=str(i)
#     # if (i//100)**3+(i//10%10)**3+(i%10)**3==i:
#     #      print(i,'水仙花')
#      if int(s[0])**3+int(s[1])**3+int(s[2])**3==i:
#          print(i)
# for i in range(1,10):
# 	for j in range(1,i+1):
# 		print('{}*{}={}'.format(i,j,i*j),end='\t')
# 	print()
#b=0
# for i in range(2,101):
# 	for j in range(2,i+1):
# 		if i%j==0:
# 			break
# 	if i==j:
# 		b=i+b
# print(b)
#b=input('字符串')
# for i in range(len(b)//2):
# 	if b[i]!=b[-i-1]:
# 		print('失败')
# 		break
# else:
# # 	print('回文字符串')
# a=('馒头','大米','小菜','米汤')
# for x,y in enumerate(a):
# 	print(x,y)
# while True:
# 	b=(input('请输入商品号'))
# 	if b=='exit':
# 		break
# 	elif type(b) !=int or b>=len(a):
# 		print('错误')
# 		continue
# 	else:
# 		b=int(b)
# 		print(a[b])
# def foe():
# 	while True:
# 		yield None
# for i in foe():
# 	print('h')#无限循环
# a=0
# i=1
# while  i<101:
# 	a=i+a
# 	i=i+1
# print(a)
#a=0
# i=0
# while i < 100:
#
# 	i=i+1
# 	a+=i
# print(a)

# while True:

#  	c=0
#  	a=input('输入数字，以逗号隔开')
#  	#a = a.split(',')
#  	if a[0] == '-':
#  		break
#  	a = a.split(',')
#  	for i in range(0,len(a)):
#  		a[i] = int(a[i])
#  		c=c+a[i]
#  	d=c/len(a)
#  	print('平均分',d)
#  	for n in a:
#  		if int(n) < d:
#  			print('低于平均分',n,end=(' '))
#  	print()
#冒泡排序法
#b=[123,345,678,34,23,67]
# a=input('数字')
# b=a.split(',')
# for i in range(0,len(b)):
#  	for j in range(0,len(b)-1):
#  		if int(b[j]) > int(b[j+1]):
#  			b[j],b[j+1]=b[j+1],b[j]
# print(b)
# a=input('列表')
# a=a.split(',')
# b=input('数字')
# b=int(b)
# for i in range(0,len(a)):
# 	for j in range(i+1,len(a)):
# 		if int(a[i])+int(a[j])==b :
#
# 			print(a[i],a[j])
# while True:
#  a=[{'name':'电脑','price':'1999'},{'name':'鼠标','price':'10'},{'name':'游艇','price':'20'},{'name':'美女','price':'998'}]
#  print(a[0],'商品序列1')
#  print(a[1],'商品系列2')
#  print(a[2],'商品序列3')
#  print(a[3],'商品序列4')
#  e=input('是否进入购物界面')
#  if int(e)==1:
#    print('成功进入')
#  elif int(e)!=1:
#   print('退出成功')
#   break
#  while True:
#       b=[]
#       c=input('输入起始资金')
#       while True:
#           d = input('输入加入购物车的商品序列号')
#           if d=='exit':
#               break
#           elif d<str(len(a)):
#               b.append(a[int(d)-1])
#               print(b)
#           else:
#               continue
#       m=input('是否结算，1为结算，其他不结算')
#       if m==str(1):
#           k=0
#           for i in range(0,len(b)):
#             k=int(b[i]['price'][0:])+k
#           print(k)
#           if k>int(c):
#                   h=int(c)-k
#                   while True:
#                      if h<0:
#                       lo=input('不够，请充值')
#
#                       h= int(h) + int(lo)
#                       print('余额：', h)
#                       if h>0:
#                           print('购买成功')
#                           break
#           elif k<int(c):
#               print('购买成功')
#       break
#字符串变整数不用int
# a=input('数字')
# m=list(a)
# m.reverse()
# c=0
# for i in range(len(m)):
#     for j in range(0,10):
#       if m[i]==str(j):
#           c=j*(10**(i))+c
# print(c)
# print(type(c))
#十进制变十六进制
# d=input('十进制数')
# a=[0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
# b=[]
# k=''
# while True:
#     c=int(d)%16
#     d=int(d)//16
#     b.append(c)
#     if d==0:
#         break
# print(b)
# for i in range(len(b)):
#      k=str(a[b[i]])+k
# print(k)

# #因数之和
# def k():
#     for i in range(1,1000):
#         b=0
#         for j in range(1,i):
#             if i%j==0:
#                 b+=j
#         if b==i:
#          print(b)
#k()











