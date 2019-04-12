#！/bin/python
#-*- coding:utf-8 -*-
import unittest
import requests
from 接口_框架.config import yanqi_peizhi
from 接口_框架.data import yanqi_shuju
class yanqi_case(unittest.TestCase):
    shuju=yanqi_shuju.dingdan_d2()
    shuju123=shuju.yanqi_shuju()
    def test_1(self):
        suo = yanqi_peizhi.dingdan_d1()
        asd = suo.yanqi_peizhi(int(self.shuju123[0][0]),int(self.shuju123[0][1]),self.shuju123[0][2],int(self.shuju123[0][3]),int(self.shuju123[0][4]),int(self.shuju123[0][5]))

        self.assertEqual(asd['status'], 'dwdwdwdwdwdw')
if __name__=='__main__':
    unittest.main()

