#！/bin/python
#-*- coding:utf-8 -*-
#统计文件多少行
# a=open(r'c:\Users\fang\Desktop\a.txt','r',encoding='utf-8')
# a1=a.readlines()
# print(len(a1))
#参数传递
#必需参数
# def abc(x,y):
#     s=0
#     for i in range(x,y):
#         for j in range(2,i+1):
#             if i%j==0:
#                 break
#         if  i==j:
#             s=s+i
#     print(s)
# abc(3,101)
#默认参数
# def abc(x=100,y=11):
#     print(x+1)
#     print(y+2)
# abc(y=111)
#可变长参数
# def abc(*args):
#     print(args)
# abc(12,22,33,'wewe','dwdwd')#元组
# def abc(x,y=10,**kwargs):
#      print(x,y,kwargs)
# abc(100,111,name='xiaohua',age=20)#字典
#计算机的基本两个数的加减乘除
# def sum(x,y):
#   return x+y
# def jian(x,y):
#     return x-y
# def cheng(x,y):
#     return x*y
# def chu(x,y):
#     return x//y
# while True:
#     a=input('>>>')
#     if '-' in  a:
#         a=a.split('-')
#         print(jian(int(a[0]),int(a[1])))
#     elif '+' in a:
#         a = a.split('+')
#         print(sum(int(a[0]), int(a[1])))
#     elif '*' in a:
#         a = a.split('*')
#         print(cheng(int(a[0]), int(a[1])))
#     elif '/' in a:
#         a = a.split('/')
#         print(chu(int(a[0]), int(a[1])))
#     else:
#         break
#lambda的基本用法
# a=lambda :4+3
# print(a())
# sum=lambda x,y:print(x+y)
# sum(11,11)
#列表推导式
# a=[i for i in range(10) if i >5]
# print(a)
#三元表达式
# a=3
# a=a+1 if a%2==1  else a
# print(a)
#导入语句
#格式1
# import 文件名
# 文件名.函数名
# import random
# a=random.randint(1,15)#随机数字
#格式2
# from day4 import sum,jia
# print(sum(8,4))
# print(jia(3,4))
import xlwt
#打开一个excel表格文件
# a=xlwt.Workbook()
# sheet=a.add_sheet('excel学习')#添加一个标签页
# #sheet.write('行','列','内容')#给sheet标签页中写入
# sheet.write(0,0,'河南')
# sheet.write(4,0,'博文')
# #保存
# a.save('软件测试.xls')
#九九乘法表
# a=xlwt.Workbook()
# sheet=a.add_sheet('excel学习')
# for i in range(1,10):
#     for j in range(1,i+1):
#         sheet.write(i-1,j-1,'{}*{}={}'.format(i,j,i*j))
# a.save('软件测试.xls')
#写入表格
# import xlwt
# c=xlwt.Workbook()
# sheet=c.add_sheet('are')
# with open(r'b.txt','r',encoding='utf-8') as a:
#    d=a.readlines()
# for i,j in enumerate(d):
#     j=j.replace('\n','').split(',')
#     print(i,j)
#     for k in range(len(j)):
#         sheet.write(i,k,j[k])
# c.save('软件测试2.xls')
#打开读取excel表格文件  xlrd
#import xlrd
#a=xlrd.open_workbook('软件测试2.xls')
# print(a.nsheets)#获取有多少个标签页
# sheet=a.sheets()[0]#根据索引获取想要操作的标签页
# print(a.sheet_names())#获取所有的标签页的名字
# new_sheet=a.sheet_by_name('are')#根据标签页的名字获取想要操作的标签页
# print(sheet.nrows)#获取标签页有多少行
# print(new_sheet.nrows)#获取标签页有多少行
# print(sheet.row_values(0))#获取标签第几行的内容，一次一行，可以用for语句
# print(sheet.ncols)#获取标签页中多少列
# print(sheet.col_values(0))#获取第几列的内容，一次一列，可以用for语句获取所有
# print(sheet.cell(1,0).value)#获取某个单元格的内容
#追加   xlutils
# import xlrd
# from xlutils.copy import copy#导入模块
# a=xlrd.open_workbook('软件测试2.xls')#打开文件
# new_a=copy(a)#复制
# sheet=new_a.get_sheet(0)#通过索引获取要操作的标签页
# sheet.write(0,3,'河南')#写入
# new_a.save('软件测试2.xls')#保存

#a.txt和b.txt中的数据导入到列表中
import xlwt
import xlrd
from xlutils.copy import copy
# c=xlwt.Workbook()
# with open(r'b.txt','r',encoding='utf-8') as a:
#     a=a.readlines()
# sheet=c.add_sheet('are')
# for i,j in enumerate(a):
#      j=j.replace('\n','').split(',')
#      for k in range(len(j)):
#          sheet.write(i,k,j[k])
# c.save('软件测试2.xls')
# m=xlrd.open_workbook('软件测试2.xls')
# oo=m.sheets()[0]
# aaa=oo.nrows
# new_m=copy(m)
# sheet=new_m.get_sheet(0)
# with open(r'a.txt','r',encoding='utf-8') as cc:
#     cc=cc.readlines()
#     for l,p in enumerate(cc):
#         p=p.replace('\n','').split(',')
#         for d in range(len(p)):
#             sheet.write(aaa+l,d,p[d])
# new_m.save('软件测试2.xls')
#从excel到txt
# import xlrd
# f=xlrd.open_workbook('软件测试2.xls')
# sheet=f.sheets()[0]
# with open(r'd.txt','w',encoding='utf-8') as cc:
#     for i in range(sheet.nrows):
#         x=','.join(sheet.row_values(i))
#         if x[-1]==',':
#             x=x.split(',')
#             x.pop(-1)
#             x=','.join(x)
#             cc.write(x+'\n')
#         elif i == (sheet.nrows-1):
#             cc.write(x)
#         else:
#             cc.write(x+'\n')
#>>>>>>>>>>>>>>>>>>>>>..
#os模块
# import os
# a=os.getcwd()
# print(a)#获取当前位置
# a=os.listdir(r'D:\Users')
# print(a)#获取目录下的所有文件，括号内可以一加路径
# os.rename('day1.py','day10.py')#更改路径，要加路径
# os.chdir(r'c：/Users/join/Desktop')#切换目录
# os.mkdir('aaa')#创建目录
# os.makedirs(r'bb\cc')#创建递归目录
# os.remove('a.txt')#删除文件
# os.rmdir('aaa')#删除空目录
# os.remove('bbb\ccc')#删除递归目录
# #################
# #执行命令(直接有结果的命令）
# abc=os.popen('arp -a')
# print(abc.read())
#将路径与文件分隔开
# a=os.path.split(r'D:\Users\fang\AppData\Local\Programs\Python_dome/day90.py')
# print(a)
# #将路径与后缀名分隔开(分隔的是字符串）
# a=os.path.splitext(r'D:\Users\fang\AppData\Local\Programs\Python_dome/day90.py')
# print(a)
#创建目录

# import os
# for i in range(10):
#      # os.mkdir('{}.txt'.format(i))
#      # print('{}.txt'.format(i))
#     os.rmdir('{}.txt'.format(i))
#正则表达式
# import re
# a='dwdsada'
#re 模块函数
# b=re.compile('d(.*)a')#将筛选条件编译
# c=re.findall('d(.*)a',a)#在全文中查找
# print(c)
# c=re.sub('sa','123',a)#在全文中替换
# b=re.compile('s(.*)g',re.S)#给.增加权限，使其可以匹配任意字符
# with open(r'd.txt','r',encoding='utf-8') as f:
#      a=f.read()
#      import re
#      #c=re.compile('1[0-9]{10}]',re.S)
#      b=re.findall('[0-9]+\.[0-9]+\.[0-9]+\.[0-9]',a)
#      print(b)
#面向对象
#将函数进行分类和封装，使开发更高效
#定义一个类
# class 储():
#     def 正(self):
#         print('小写变大写')
#     def 世(self):
#         储.正()
#         print('壹加壹')
#     def 府(self):
#         self.正()#叫类的实例，方便在类的内部调用函数
#         print('走了')
# class 奇():
#     def 倾(self):
#         print('谐')
# ##原本的调用函数为储().世()
# 储=储()#叫类的实例，方便在类的外部调用函数
# 储.世()
#继承：在类后面的括号里添加其他的类名：代表继承了此类名的所有函数，也可以一次继承多个类的函数，在类名之间用逗号隔开例子：class a(类名1,类名2,类名3):
#在继承的过程中采用就近原则，也就是在继承的中不同类中有相同的函数，调用函数的结果为继承时第一个出现函数的类的结果
#多态，方法重写：在继承类的时候发现某个函数错误解决为在自身类的下面重新写一个这个函数，本着先采用就近原则会先采用自身下的函数。
#私有方法（属性）：不能被继承的方法，只能在自己的类的内部使用：在函数名的左边添加两个下划线：def __a(self):
#类的专有方法
#1：__init__
# class 储():
#     name='小红'#类的属性
#     def __init__(self,x):#类的专有方法之初始化属性（即为更改属性）
#         self.name=x
#     def 正(self):
#         print('hello {}'.format(self.name))
#     def 世(self):
#         print('{}今年18'.format(self.name))
#     def 府(self):
#         print('走了')
# a=储('小鬼')
# b=储('小傻')
# a.正()
# b.世()
#####多线程
###同步io：          异步io
#######异步io  例子：：：
# from time import sleep
# import threading
# def asd():
#     for i in range(3):
#         print('打篮球')
#         sleep(4)
# def asr():
#     for j  in range(3):
#         print('送饮料')
#         sleep(2)
# threading.Thread(target=asd).start()
# threading.Thread(target=asr).start()
import time
#显示时间，以元组的形式
# print(time.localtime())
# #按现代化的格式显示时间也叫格式化时间
# abc=time.localtime()
# print(time.strftime('%Y-%m-%d %H:%M:%S %a %j',abc))
######时间戳  从公元1970年到现在所经过的秒数
# bb=time.time()
# print(bb)
# print(time.strptime('1989-01-23','%Y-%H-%j'))
#############发送邮件
# import smtplib   #连接邮件服务器
# import email.mime.multipart   #处理邮件的组成
# import email.mime.text    #处理邮件正文
# import xlrd
#
# server='smtp.163.com'   #邮件服务器
# from_user='17530132553@163.com'
# res= '1562065932@qq.com'
# passwd='f950302'    #授权码   允许登陆客户端的密码
#
# ####创建一个空的邮件
#
# message=email.mime.multipart.MIMEMultipart()
# ####邮件的发件人#
# message['from']=from_user
# ###邮件的接受者
# message['To']=res
# ######邮件的主题
# message['subject']='python learn'
# ####邮件的内容
# text= """
# 中国，你
# 希望你不要令我失望
# """
# ######对正文进行编码
# text=email.mime.text.MIMEText(text,'plain','utf-8')
# #######带附件的邮件需要添加以下代码
#
# #####将正文添加到邮件中
# message.attach(text)
# #######对附件进行读取进行编码
# att2=email.mime.text.MIMEText(open('kai.jpg','rb').read(),'base64','utf-8')
# ####给附件添加头部信息
# att2["content-type"] = 'application/octet-stream'
# att2["Content-Disposition"]='attachment;filename="kai.jpg"'
# message.attach(att2)
# ####连接服务器kai.jpg
# smtp123=smtplib.SMTP_SSL(server,465)
# #####登陆服务器
# smtp123.login(from_user,passwd)
# #####发送邮件
# smtp123.sendmail(from_user,res,message.as_string())
# #######断开连接
# smtp123.close()
# ########采用ssh协议，连接linux 并管理
#创建一个远程客户端
# import paramiko
# ssh123=paramiko.SSHClient()
# #第一次连接主机，known_hosts 存放的主机地址，跳过查找
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# #连接主机
# ssh123.connect(hostname='192.168.0.102',
#                port=22,
#                username='root',
#                password='950302')
# #执行命令  exec_command 只能执行有结果的命令
# a,d,c=ssh123.exec_command('ls -al')
# print(d.read().decode())
# #a,d,c三个变量的解析，1 表示输入的命令  2  命令的结果  3 命令的报错
# ssh123.close()
######传输文件
# import paramiko
# #建立一个传输通道
# ssh123=paramiko.Transport('192.168.0.102')
# #连接linux
# ssh123.connect(username='root',password='950302')
# #创建一个传输文件的对象
# sftp=paramiko.SFTPClient.from_transport(ssh123)
# # #从linux到windows传文件，括号中第一个参数为下载的文件，第二个为存到的文件名和路径
# # sftp.get('install.log',r'.\abc.log')##
##下载
# # ssh123.close()
# ######从windows到linux
# sftp.put('jb_python.py',r'/home/jb_python.py')###上传
# ssh123.close()
# #注：：：.get是下载， .put是上传
# ########################
#socket（套接字）：是实现最底层的一种通信方式， 接受   发送      。采用c/s架构
#通过tcp协议进行通信   socket
#server端，服务器端
# import socket
# #创建一个套接字,并且使用tcp协议,ip版本ipv4
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #绑定ip，端口号，接受的是一个元祖
# s.bind(('127.0.0.1',8888))
# #监听服务是否开启，数字指的是最大等待数
# s.listen(3)
# while True:
#     #接受请求,两个变量  1 接受信息   2  客户端ip和端口号
#     conn,addr=s.accept()
#     #接受数据 1024表示一次最大能接受1024字节数据
#     reg=conn.recv(1024)
#     print(reg.decode('utf-8'))
#     #发送数据
#     a=input('>>>>')
#     conn.send(a.encode('utf-8'))
#########包：是一个目录，是一类模块的集合，都必须含有__int__.py文件
#模块：是一个.py文件，是一类函数或者类的集合
##创建包
##导入包。 form aaa.day9 import asd或者from aaa import day9  aa=aaa.asd() aa.函数名（）
##########################################################
##socket   udp传输
###server端
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定主机
s.bind(('127.0.0.1',8888))
while True:
    ###接收数据 第一个变量：客户端的请求数据  第二个变量：客户端的ip和端口号
    conn,addr=s.recvfrom(1024)
    print(conn.decode('utf-8'))
    ##发送响应
    a=input('>>>>')
    s.sendto(a.encode('utf-8'),addr)



















