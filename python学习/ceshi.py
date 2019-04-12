#！/bin/python
#-*- coding:utf-8 -*-
######接口，对接口传参和结果对比
##http协议    request模块
import requests
import json
import unittest
import time
import HTMLTestRunner
##必须面向对象写
# class suopei(unittest.TestCase):
#     def test_1(self):
#         url='https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
#         head={
#              "Content-Type":"application/json",
#              "x-dealer-code":"2100150",
#              "x-position-code":"D_PO_1028",
#              "x-resource-code":"BASIC_DATA",
#              "x-track-code":"4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
#              "x-user-code":"djy0mx",
#              "x-access-token":"da05ee37e5676e7b27972b2892e0fdeb"
#          }
#         body='{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize":10,"curPage": 1}'.encode('utf-8')
#         res=requests.post(url,headers=head,data=body)
#         mes=json.loads(res.text)
#         self.assertEqual(mes['data']['applicationType'][0]['name'],'多装')
#     def test_2(self):
#         url = 'https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
#         head = {
#             "Content-Type": "application/json",
#             "x-dealer-code": "2100150",
#             "x-position-code": "D_PO_1028",
#             "x-resource-code": "BASIC_DATA",
#             "x-track-code": "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
#             "x-user-code": "djy0mx",
#             "x-access-token": "da05ee37e5676e7b27972b2892e0fdeb"
#         }
#         body = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize":10,"curPage": 1}'.encode(
#             'utf-8')
#         res = requests.post(url, headers=head, data=body)
#         mes = json.loads(res.text)
#         self.assertNotEqual(mes['data']['applicationType'][0]['name'],'装')
#     def test_3(self):
#         url = 'https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
#         head = {
#             "Content-Type": "application/json",
#             "x-dealer-code": "2100150",
#             "x-position-code": "D_PO_1028",
#             "x-resource-code": "BASIC_DATA",
#             "x-track-code": "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
#             "x-user-code": "djy0mx",
#             "x-access-token": "da05ee37e5676e7b27972b2892e0fdeb"
#         }
#         body = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize":10,"curPage": qwe}'.encode(
#             'utf-8')
#         res = requests.post(url, headers=head, data=body)
#         mes = json.loads(res.text)
#         self.assertIn('多装', ['多装','DSD','看看'])
# if __name__=='__main__':
#     ######main，是检测类中所有以test开头的函数，去执行，没一个test就是一个测试用例，
#     ######main的执行顺序是以test后面的字符，谁在前面执行谁
#     #unittest.main()
#     ###创建一个测试套件
#     suit=unittest.TestSuite()
#     ####添加测试用例
#     for i in range(1,4):
#         suit.addTest(suopei('test_{}'.format(i)))
#     now=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
#     f=open('abc.html','wb')
#     #########定义测试报告的内容
#
#     runner=HTMLTestRunner.HTMLTestRunner(
#         stream=f,title='索赔测试报告',tester='方',description='结果如下'
#     )
#     ###执行套件
#     runner.run(suit)
#     f.close()
##############


