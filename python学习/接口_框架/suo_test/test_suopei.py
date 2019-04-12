#！/bin/python
#-*- coding:utf-8 -*-
import unittest
import requests
from 接口_框架.config import aaaa
from 接口_框架.data import suopei_duqu
class suopei_case(unittest.TestCase):
    shuju=suopei_duqu.suopei_shuju()
    shuju123=shuju.dequ_jichu()
    def test_1(self):
        suo=aaaa.Suopei()
        asd=suo.jichu_shuju(int(self.shuju123[0][0]),int(self.shuju123[0][1]))
        self.assertEqual(asd['data']['applicationType'][0]['name'],'多装')
    def test_2(self):
        suo = aaaa.Suopei()
        asd = suo.jichu_shuju(self.shuju123[1][0],int(self.shuju123[1][1]))
        self.assertEqual(asd['message'],'get error')
    def test_3(self):
        suo = aaaa.Suopei()
        asd = suo.jichu_shuju(int(self.shuju123[2][0]), self.shuju123[2][1])
        self.assertEqual(asd['message'], 'get error')
if __name__=='__main__':
    unittest.main()



