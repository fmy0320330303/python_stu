
#########################################################################################################
#爬图片写入到文件txt
#过滤图片的网址
# import requests
# import re
# import os
# class 糗事_spider(object):
#     a=0
#     def 发送请求(self,page):
#         ur='https://www.qiushibaike.com/imgrank/page/{}/'.format(page)
#         head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'}
#         响应=requests.get(url=ur,headers=head)
#         html=响应.content.decode('utf-8')
#         return html
#     def guolv(self,abc):
#         shuju=[]
#         patt=re.compile(r'<img src="//pic.qiushibaike.com/system/pictures/(.*?).jpg"',re.S)
#         items=patt.findall(abc)
#         for i in  items:
#             i='https://pic.qiushibaike.com/system/pictures/'+i+'.jpg'
#             shuju.append(i)
#         return shuju
#     def save(self,qwe):
#             #任何图片都是二进制
#             #请求图片的网址，得到图片的源码
#         for i in qwe:
#             res=requests.get(i)
#             html=res.content#读取的是二进制
#             with open(r'C:\Users\fang\Desktop\python学习\pup\{}.jpg'.format(self.a),'wb') as f:
#                 f.write(html)
#             self.a+=1
#     def shanchu(self):
#         kk=os.listdir(r'C:\Users\fang\Desktop\python学习\pup')
#         for i in kk:
#             os.remove(r'C:\Users\fang\Desktop\python学习\pup\{}'.format(i))
# a=糗事_spider()
# # for i in range(1,4):
# #     html = a.发送请求(page=i)
# #     shuju=a.guolv(abc=html)
# #     a.save(shuju)
# a.shanchu()#执行的是上面的几个函数的结果删掉
#################################################################################################
###爬文字
import requests
import re
# class 糗事_spider(object):
#     def 发送请求(self,page):
#         ur='https://www.qiushibaike.com/text/page/{}/'.format(page)
#         #伪装浏览器
#         head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'}
#         #发送请求的代码
#         响应=requests.get(url=ur,headers=head)
#         #读取响应1.text 2.content
#         #print(响应.content.decode('utf-8'))
#         html=响应.content.decode('utf-8')
#         return html
#     def 过滤(self,abc):
#         shuju=[]
#         #将正则表达式编译
#         patt=re.compile(r'<div class="content">(.*?)</span>',re.S)
#         #将编译后的条件到字符串中查找
#         items=patt.findall(abc)
#         for i in items:
#             i=i.replace('<span>','').replace('<br/>','').strip()
#             shuju.append(i)
#         return shuju
#     def save(self,qwe):
#         with open('a.txt','a',encoding='utf-8') as f:
#             for i in qwe:
#                 f.write(i+'\n')
# a=糗事_spider()
# for i in range(1,6):
#     html = a.发送请求(page=i)
#     shuju=a.过滤(abc=html)
#     a.save(shuju)
######################################################################################################
#和数据库的交互
# import pymysql
# conn=pymysql.connect(host='192.168.0.102',
#                      port=3306,
#                      user='root',
#                      password='123456',
#                      charset='utf8')
# abc=conn.cursor()
# #abc.execute('create database fang5')
# abc.execute('show databases;')
# abc.execute('use fang5;')
# abc.execute('show tables;')
# #print(abc.fetchall())
# #abc.execute('create table biao5(name char(20),age char(30), sex char(30),pingjia char(30));')
# # import xlwt
# # import xlrd
# # a=xlrd.open_workbook('电影信息.xls')
# # sheet=a.sheets()[0]
# # for i in range(sheet.nrows):
# #     a=sheet.row_values(i)
# #     #print(a)
# #     abc.execute('insert into biao5 values("{}","{}","{}","{}");'.format(a[0],a[1],a[2],a[3]))
# #     conn.commit()
# abc.execute('select * from biao5;')
# print(abc.fetchall())

######承接以上对连接数据库的注释和操作
# #abc.execute('insert into biao1 values("xiaogui","20","nan"),("xiaohong","18","nv");')#可以for循环写入，填充写入
# ###对数据库进行更改的时候需要提交一下
# ###是由连接数据库的变量来提交
# conn.commit()
# abc.execute('select * from biao1')
# #print(abc.fetchall())#接受上一句的结果的
# print(abc.fetchmany(5))#接受上一个sql语句的结果，默认只接受第一行，在括号中写入数字几，就接受多少行
# #print(abc.fetchone())#只接受一行，与readline相同，一次一行，下一次下一行
# conn.close()#断开数据库
# while True:
#     try:
#         a=input('>>>')
#         if a=='exit':
#             break
#         else:
#             abc.execute('{}'.format(a))
#             print((abc.fetchall()))
#     except:
#         continue
# conn.close()
################
#爬网址的写入到except
# import re
# import requests
# import xlwt
# from xlutils.copy import copy
# import xlrd
# class  doubai_Spider(object):
#     def fasong(self,p25):
#         ur='https://movie.douban.com/top250?start=%s&filter='%(p25)
#         head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'}
#         qing=requests.get(url=ur,headers=head)
#         html=qing.content.decode('utf=8')
#         return html
#     def  guolv(self,html):
#         patt=re.compile('<div class="pic">(.*?)</li>',re.S)
#         patc=patt.findall(html)
#         for i in range(5):
#             if i ==1:
#                 mingcheng=re.compile(' <img width="100" alt="(.*?)" src',re.S)
#                 mingcheng2=mingcheng.findall(str(patc))
#             elif i==2:
#                 daoyan=re.compile('导演: (.*?)&nbsp',re.S)
#                 daoyan2=daoyan.findall(str(patc))
#             elif i==3:
#                 miaoshu=re.compile('<span class="inq">(.*?)</span>',re.S)
#                 miaoshu2=miaoshu.findall(str(patc))
#             elif i==4:
#                 renshu=re.compile('<span>(.*?)人评价</span>',re.S)
#                 renshu2=renshu.findall(str(patc))
#         return mingcheng2,daoyan2,miaoshu2,renshu2
#     def baocun(self,guol,p2):
#         f=xlrd.open_workbook('电影信息.xls')
#         new_f=copy(f)
#         sheet=new_f.get_sheet(0)
#         for  j in range(len(guol)):
#             for k,l in enumerate(guol[j]):
#                 sheet.write(k+1+p2,j,l)
#         new_f.save('电影信息.xls')
# xinjian=xlwt.Workbook(encoding='utf-8')
# sheet=xinjian.add_sheet('excel电影')
# sheet.write(0,0,'名称')
# sheet.write(0,1,'导演')
# sheet.write(0,2,'描述')
# sheet.write(0,3,'评价人数')
# xinjian.save('电影信息.xls')
# a=doubai_Spider()
# for h in range(0,75,25):
#     html=a.fasong(h)
#     patc=a.guolv(html)
#     a.baocun(patc,p2=h)
###############连接linux
# import paramiko
# def lin():
#     with paramiko.SSHClient() as f:
#         f.set_missing_host_key_policy(paramiko.AutoAddPolicy)
#         f.connect(hostname='192.168.0.102',
#                   port='22',
#                   username='root',
#                   password='950302')
#         while True:
#             a=input('输入命令')
#             if a=='exit':
#                 break
#             else:
#                 a,b,c=f.exec_command('{}'.format(a))
#                 print(b.read().decode())
# lin()
# a=[1,2,3,4]
# b=[11,22,33,44]
# c=[111,222,333]
# d=list(zip(c,b,a))
# print(d)
import time
b=time.strptime('2000-1-22','%Y-%m-%d')
a=time.mktime(b)
c=a-86400
d=time.localtime(c)
ck=time.strftime('%Y-%m-%d %H:%M:%S',d)
print(ck)
