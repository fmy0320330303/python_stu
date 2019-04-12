#！/bin/python
#-*- coding:utf-8 -*-
import requests
import json
import unittest
import HTMLTestRunner
from appium import webdriver
from  time import  sleep
import warnings
class  dingdan_d1(object):
    def yanqi_peizhi(self,a,b,c,d,e,m):
        url='https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/delayOrderCancelStatus/getCancelDelayOrder'
        head={'Content-Type':'application/json','x-dealer-code':'2100001',
            'x-position-code':'D_PO_1028','x-resource-code':'pol4s_delayOrderCancelStatus_getCancelDelayOrder',
            'x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394','x-user-code':'dhxc1u',
            'x-access-token':'da05ee37e5676e7b27972b2892e0fdeb'}
        body='{"pageNum": %s,"pageSize": %s,"queryTerms": {"orderNo":"%s","cancelStatus":%s,"applyStartDate":%s,"applyEndDate":%s}}'%(a,b,c,d,e,m)
        body = body.encode('utf-8')
        res = requests.post(url, headers=head, data=body)
        mes = json.loads(res.text)
        return mes
    def shouye_zhuangtai(self):
        url='https://mobileqa.dms.saic-gm.com/api/dev/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderHomePage'
        head={
            'Content-Type': "application/json",
            'x-dealer-code': "2100005",
            'x-position-code': "D_PO_1028",
            'x-resource-code': "pol4s_partOrder_orderHomePage",
            'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            'x-user-code': "dhxc1u",
            'x-access-token': "0da5606a534fa727dfd7f502df38be65",
            'cache-control': "no-cache",
            'Postman-Token': "3708ccbb-25c7-44be-b74a-bb6aa05ec848"
        }
        res=requests.post(url=url,headers=head)
        return res.json()

    def chaxun_dingdan(self,a,b):
        url='https://mobileqa.dms.saic-gm.com/api/dev/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderList'
        head={
            'Content-Type': "application/json",
            'x-dealer-code': "2100001",
            'x-position-code': "D_PO_1028",
            'x-resource-code': "pol4s_partOrder_orderList",
            'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            'x-user-code': "dhxc1u",
            'x-access-token': "0da5606a534fa727dfd7f502df38be65",
            'cache-control': "no-cache",
            'Postman-Token': "e99dd8d3-7074-4b85-9b92-fec6aaa154f8"
        }
        body='{"pageNum": %s,"pageSize": %s,"queryTerms": {"orderType": "","orderStatus": "","orderDelayFlag": "","orderNo": "","startReportDate": "","endReportDate": ""}}' %(a,b)
        body=body.encode('utf-8')
        res=requests.post(url=url,headers=head,data=body)
        return res.json()

    def peijian_mingxi(self,a):
        url='https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderPartDetail'
        head={
            'Content-Type': "application/json",
            'x-dealer-code': "2100001",
            'x-position-code': "D_PO_1028",
            'x-resource-code': "pol4s_partOrder_orderPartDetail",
            'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            'x-user-code': "dhxc1u",
            'x-access-token': "0da5606a534fa727dfd7f502df38be65",
            'cache-control': "no-cache",
            'Postman-Token': "00587d6d-f948-4bbf-a39e-892ca095a9a3"
        }
        body='{"partOrderItemId":%s}' % (a)
        body=body.encode('utf-8')
        res=requests.post(url=url,headers=head,data=body)
        return res.json()

    def dingdan_mingxi(self,a,b,c):
        url='https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrderSearch/partOrderDetailSearch'
        head={
            'Content-Type': "application/json",
            'x-dealer-code': "2100005",
            'x-position-code': "D_PO_1028",
            'x-resource-code': "pol4s_partOrderSearch_partOrderDetailSearch",
            'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            'x-user-code': "dhxc1u",
            'x-access-token': "0da5606a534fa727dfd7f502df38be65",
            'cache-control': "no-cache",
            'Postman-Token': "ccd2b6f8-5d64-4cce-97e1-53e54498aa6d"
        }
        body='{"pageNum":%s,"pgeSize":%s,"queryTerms":{"orderNo":%s}}' %(a,b,c)
        body=body.encode('utf-8')
        res=requests.post(url=url,headers=head,data=body)
        return res.json()
    def  zheda_peizhi(self,a,b):
        warnings.simplefilter("ignore", ResourceWarning)
        desired_caps = {'platformName': 'Android',
                        'deviceName': '127.0.0.1:62001',
                        'appPackage': 'net.crigh.cgapp_schedule',
                        'appActivity': '.activity.login.LoginActivity'}
        dr=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        sleep(15)
        dr.find_element_by_id('net.crigh.cgapp_schedule:id/editLoginUserName').send_keys(a)
        sleep(4)
        dr.find_element_by_id('net.crigh.cgapp_schedule:id/editLoginUserPas').send_keys(b)
        sleep(4)
        dr.find_element_by_id('net.crigh.cgapp_schedule:id/btnLogin').click()
        sleep(4)
        mm=dr.find_element_by_class_name('android.widget.TextView').text
        return mm



