#!/usr/bin/python
#-*- coding:utf-8 -*-
import unittest
from 接口_框架.config import yanqi_peizhi
from 接口_框架.data import  yanqi_shuju

class zuoye_test(unittest.TestCase):
    shuju=yanqi_shuju.dingdan_d2()
    shuju=shuju.chaxun_1canshu()

    def test_chaxundingdan_1(self):
        suo=yanqi_peizhi.dingdan_d1()
        asd=suo.chaxun_dingdan(int(self.shuju[0][0]),int(self.shuju[0][1]))
        self.assertEqual(asd['status'],1)

    def test_chaxundingdan_2(self):
        suo=yanqi_peizhi.dingdan_d1()
        asd=suo.chaxun_dingdan((self.shuju[1][0]),int(self.shuju[1][1]))
        self.assertEqual(asd['message'],'get error')

    def test_chaxundingdan_3(self):
        suo=yanqi_peizhi.dingdan_d1()
        asd=suo.chaxun_dingdan(int(self.shuju[2][0]),(self.shuju[2][1]))
        self.assertEqual(asd['message'],'get error')

    def test_chaxundingdan_4(self):
        suo = yanqi_peizhi.dingdan_d1()
        asd = suo.chaxun_dingdan((self.shuju[3][0]), int(self.shuju[3][1]))
        self.assertEqual(asd['message'],'get error')

    def test_chaxundingdan_5(self):
        suo = yanqi_peizhi.dingdan_d1()
        asd = suo.chaxun_dingdan(int(self.shuju[4][0]), (self.shuju[4][1]))
        self.assertEqual(asd['message'],'get error')

if __name__ =='__main__':
    unittest.main()