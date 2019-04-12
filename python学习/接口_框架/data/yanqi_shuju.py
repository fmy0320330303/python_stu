#！/bin/python
#-*- coding:utf-8 -*-
import xlrd
class dingdan_d2(object):
    def yanqi_shuju(self):
        shuju = []
        f = xlrd.open_workbook(r'C:\Users\fang\Desktop\python学习\接口_框架\data\yanqi_shuju.xlsx')
        sheet = f.sheets()[0]
        num = sheet.nrows
        for i in range(num):
            if i == 0:
                continue
            else:
                shuju.append(sheet.row_values(i))
        return shuju
    def chaxun_1canshu(self):
        shuju = []
        f = xlrd.open_workbook(r'C:\Users\fang\Desktop\python学习\接口_框架\data\查询订单.xlsx')
        sheet = f.sheets()[0]
        for i in range(sheet.nrows):
            if i == 0:
                continue
            else:
                shuju.append(sheet.row_values(i))
        return shuju

    def peijian_2canshu(self):
        shuju = []
        f = xlrd.open_workbook(r'C:\Users\fang\Desktop\python学习\接口_框架\data\配件明细.xlsx')
        sheet = f.sheets()[0]
        for i in range(sheet.nrows):
            if i == 0:
                continue
            else:
                shuju.append(sheet.row_values(i))
        return shuju

    def dingdan_3canshu(self):
        shuju = []
        f = xlrd.open_workbook(r'C:\Users\fang\Desktop\python学习\接口_框架\data\订单明细.xlsx')
        sheet = f.sheets()[0]
        for i in range(sheet.nrows):
            if i == 0:
                continue
            else:
                shuju.append(sheet.row_values(i))
        return shuju
    def zheda_shuju(self):
        shuju=[]
        f=xlrd.open_workbook(r'C:\Users\fang\Desktop\python学习\接口_框架\data\浙大教室.xlsx')
        sheet=f.sheets()[0]
        for i in range(sheet.nrows):
            if i == 0:
                continue
            else:
                shuju.append(sheet.row_values(i))
        return shuju

if __name__ == '__main__':
    u=dingdan_d2().peijian_2canshu()
    print(u)



