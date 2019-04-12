#！/bin/python
#-*- coding:utf-8 -*-
import xlrd
class suopei_shuju(object):
    def dequ_jichu(self):
        shuju=[]
        f=xlrd.open_workbook(r'C:\Users\fang\Desktop\python学习\接口_框架\data\suopei.xlsx')
        sheet=f.sheets()[0]
        num=sheet.nrows
        for i in range(num):
            if i==0:
                continue
            else:
                shuju.append(sheet.row_values(i))
        return shuju


