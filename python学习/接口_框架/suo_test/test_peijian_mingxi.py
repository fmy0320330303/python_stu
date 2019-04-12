#!/usr/bin/python
#-*- coding:utf-8 -*-


import unittest
from 接口_框架.config import yanqi_peizhi
from  接口_框架.data import yanqi_shuju

class zuoye_test(unittest.TestCase):

    shuju=yanqi_shuju.dingdan_d2()
    shuju=shuju.yanqi_shuju()

    def test_peijianmingxi_1(self):
        suo=yanqi_peizhi.dingdan_d1()
        asd=suo.peijian_mingxi(int(self.shuju[0][0]))
        self.assertEqual(asd['status'],1)

    def test_peijianmingxi_2(self):
        suo=yanqi_peizhi.dingdan_d1()
        asd=suo.peijian_mingxi(self.shuju[1][0])
        self.assertEqual(asd['message'],'get error')

    def test_peijianmingxi_3(self):
        suo=yanqi_peizhi.dingdan_d1()
        asd=suo.peijian_mingxi((self.shuju[2][0]))
        self.assertEqual(asd['message'],'get error')

    def test_peijianmingxi_4(self):
        suo=yanqi_peizhi.dingdan_d1()
        asd=suo.peijian_mingxi((self.shuju[3][0]))
        self.assertEqual(asd['message'],'get error')

    def test_peijianmingxi_5(self):
        suo=yanqi_peizhi.dingdan_d1()
        asd=suo.peijian_mingxi((self.shuju[4][0]))
        self.assertEqual(asd['message'],'get error')


if __name__ =='__main__':
    unittest.main()