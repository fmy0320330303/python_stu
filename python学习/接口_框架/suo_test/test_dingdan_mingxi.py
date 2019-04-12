#!/usr/bin/python
#-*- coding:utf-8 -*-
import unittest
from 接口_框架.config import yanqi_peizhi
from  接口_框架.data import yanqi_shuju
class zuoye_test(unittest.TestCase):

    shuju=yanqi_shuju.dingdan_d2()
    shuju123=shuju.dingdan_3canshu()


    def test_dingdanmingxi_1(self):
        suo=yanqi_peizhi.dingdan_d1()
        asd=suo.dingdan_mingxi(int(self.shuju123[0][0]),int(self.shuju123[0][1]),(self.shuju123[0][2]))
        self.assertEqual(asd['status'], 1)

    def test_dingdanmingxi_2(self):
        suo=yanqi_peizhi.dingdan_d1()
        asd=suo.dingdan_mingxi((self.shuju123[1][0]),int(self.shuju123[1][1]),(self.shuju123[1][2]))
        self.assertEqual(asd['message'],'get error')

    def test_dingdanmingxi_3(self):
        suo =yanqi_peizhi.dingdan_d1()
        asd = suo.dingdan_mingxi(int(self.shuju123[2][0]), (self.shuju123[2][1]), (self.shuju123[2][2]))
        self.assertEqual(asd['message'], 'get error')

    def test_dingdanmingxi_4(self):
        suo = yanqi_peizhi.dingdan_d1()
        asd = suo.dingdan_mingxi(int(self.shuju123[3][0]), int(self.shuju123[3][1]), (self.shuju123[3][2]))
        self.assertEqual(asd['errMsg'], '该订单号对应的订单不存在！')

    def test_dingdanmingxi_5(self):
        suo = yanqi_peizhi.dingdan_d1()
        asd = suo.dingdan_mingxi((self.shuju123[4][0]), int(self.shuju123[4][1]), (self.shuju123[4][2]))
        self.assertEqual(asd['message'], 'get error')


if __name__ == '__main__':
    unittest.main()