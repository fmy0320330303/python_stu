#！/bin/python
#-*- coding:utf-8 -*-
# def sum(x,y):
#     a=x//y
#     return a
# def jia(x,y):
#     b=x+y
#     return b
# if __name__=='__main__':
#     a=input('数字')
#     m=list(a)
#     m.reverse()
#     c=0
#     for i in range(len(m)):
#         for j in range(0,10):
#             if m[i]==str(j):
#                 c=j*(10**(i))+c
#     print(c)
# if __name__=='__main__':
#     print('hello')
#     print(c)
# def a(x,y,z):
#     c=''
#     for i in range(len(x)):
#         if i<y:
#             c=c+x[i]
#         elif i>=y+z:
#             c=c+x[i]
#     return print(c)
# a('qwert',2,7)
#对爬虫的练习
import requests
import re
# class a(object):
#     def b(self,page):
#         ur='https://www.qiushibaike.com/textnew/page/{}/?s=5167697'.format(page)
#         head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'}
#         res=requests.get(url=ur,headers=head)
#         html=res.content.decode('utf-8')
#         return html
#     def c(self,d):
#         e=[]
#         patt=re.compile(r'<div class="content">(.*?)</div>',re.S)
#         items=patt.findall(d)
#         for i  in items:
#             i=i.replace('</span>','').replace('<span>','').replace('<br/>','').replace('\u3000\u3000','').strip()
#             e.append(i)
#         return e
#     def m(self,ss):
#         f=open(r'b.txt','w',encoding='utf-8')
#         for i in ss:
#             f.write(i+'\n')
# a1=a()
# html=a1.b(2)
# e=a1.c(d=html)
# a1.m(e)
import xlrd
import xlwt
import json
import xlutils
import requests
import re
import os
from xlutils.copy import copy
# class zhilian(object):
#     def qingqiu(self):
#         ur='https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=530&workExperience=0103&education=5&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=软件测试工程师&kt=3&' \
#            '_v=0.49259441&x-zp-page-request-id=5be78b9216fd40c69af7560d8fff50f2-1550668431041-350711'
#         herd={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'}
#         res=requests.get(url=ur,headers=herd)
#         html=res.content.decode('utf-8')
#         return html
#     def guolv(self,abc):
#         bbb=[]
#         ddd=[]
#         for i in range(len(abc['data']['results'])):
#             bb=abc['data']['results'][i]['company']['name']
#             bbb.append(bb)
#         for j in range(len(abc['data']['results'])):
#             dd = abc['data']['results'][i]['salary']
#             ddd.append(dd)
#         return bbb,ddd
#     def baocun(self,cc):
#         f = xlwt.Workbook(encoding='utf-8')
#         sheet = f.add_sheet('求职')
#         sheet.write(0, 0, '公司')
#         sheet.write(0, 1, '薪资')
#         f.save('小鬼.xls')
#         f=xlrd.open_workbook('小鬼.xls')
#
#         new_f = copy(f)
#         sheet=new_f.get_sheet(0)
#
#         for i in range(len(cc)):
#             for m,j in enumerate(cc[i]):
#                 sheet.write(m+1,i,j)
#         new_f.save('小鬼.xls')
# f=xlwt.Workbook(encoding='utf-8')
# sheet = f.add_sheet('求职')
# sheet.write(0, 0, '公司')
# sheet.write(0, 1, '薪资')
# f.save('小鬼.xls')
# a=zhilian()
# aaa=a.qingqiu()
# abc=json.loads(aaa)
# cc=a.guolv(abc)
# a.baocun(cc)
# class zixun(object):
#     a=0
#     def qingqiu(self,page):
#         ur='https://www.doutula.com/article/list/?page={}&tdsourcetag=s_pcqq_aiomsg'.format(page)
#         head={'User - Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'}
#         res=requests.get(url=ur,headers=head)
#
#         html=res.content.decode('utf-8')
#         return html
#     def guolv(self,aaa):
#         patt=re.compile('<a href="(.*?)" class="list-group-item random_list')
#         items=patt.findall(aaa)
#         return items
#     def baocun(self,qwe):
#         print(len(qwe))
#         shu=[]
#         for i in qwe:
#                  res=requests.get(i)
#                  html=res.content.decode('utf-8')
#
#                  htm= re.compile('this.src=\'(.*?)\'">')
#                  it = htm.findall(html)
#                  shu.append(it)
#         for j in range(len(shu)):
#             for k in range(len(shu[j])):
#                 eee = requests.get(shu[j][k])
#                 pp= eee.content
#                 if shu[j][k][-1]=='g':
#                     with open(r'C:\Users\fang\Desktop\python学习\pup\{}.jpg'.format(self.a),'wb') as f:
#                         f.write(pp)
#                         self.a+=1
#                 else:
#                     with open(r'C:\Users\fang\Desktop\python学习\pup\{}.gif'.format(self.a), 'wb') as f:
#                         f.write(pp)
#                         self.a += 1
#
#
#     # def shanchu(self):
#     #     kk=os.listdir(r'C:\Users\fang\Desktop\python学习\pup')
#     #     for i in kk:
#     #         os.remove(r'C:\Users\fang\Desktop\python学习\pup\{}'.format(i))
# a=zixun()
# for i in range(1,3):
#     aaa=a.qingqiu(i)
#     a.guolv(aaa)
#     a.baocun(a.guolv(aaa))
# #a.shanchu()
#client  客户端  tcp 传输
# while True:
#     import socket
#     sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     #连接服务器
#     sock.connect(('127.0.0.1',8888))
#     #发送请求
#     a=input('请求数据')
#     sock.send(a.encode('utf-8'))
#     #接受数据
#     msg = sock.recv(1024)
#     if msg.decode('utf-8')=='exit':
#         break
#         sock.close()
#     else:
#         print(msg.decode('utf-8'))
#     # #断开连接
#     # sock.close()
#####client  客户端   udp传输
import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
###发送请求
# host=('127.0.0.1',8888)
# while True:
#     a=input('>>>>')
#     if a!='exit':
#         sock.sendto(a.encode('utf-8'),host)
#         ##W接受数据
#         msg=sock.recv(1024)
#         print(msg.decode('utf-8'))
#     else:
#         break
# #sock.close()
