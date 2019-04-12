#！/bin/python
#-*- coding:utf-8 -*-
import unittest
import requests
from 接口_框架.config import yanqi_peizhi
from 接口_框架.data import yanqi_shuju
class zheda_case(unittest.TestCase):
    shuju = yanqi_shuju.dingdan_d2()
    shuju123 = shuju.zheda_shuju()
    def test_1(self):
        suo = yanqi_peizhi.dingdan_d1()
        asd = suo.zheda_peizhi(int(self.shuju123[0][0]),int(self.shuju123[0][1]))
        self.assertEqual(asd,'浙大教室')

if __name__=='__main__':
    unittest.main()




