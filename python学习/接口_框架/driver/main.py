#！/bin/python
#-*- coding:utf-8 -*-
from 接口_框架.report.baogao import baogao_
def run(aa):
    baogao_(aa)
##run('test_suopei.py')
with open('回归.txt','r') as f:
    a=f.readlines()
    if a=='all':
        run('*')
    else:
        run(a)
