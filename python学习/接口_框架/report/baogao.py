#！/bin/python
#-*- coding:utf-8 -*-
import HTMLTestRunner
import unittest
from 接口_框架.suo_test.test_suopei import suopei_case

def baogao_(aa):
    suit=unittest.TestSuite()####测试套件
    #####可以导入一个类名
    #suit.addTest(unittest.makeSuite(suopei_case))
    ######需要两个参数，参数1为路径，参数2为正则，匹配条件
    ##到这个路径下匹配以test开头的所以文件
    for o in  aa:
        dis=unittest.defaultTestLoader.discover(r'C:\Users\fang\Desktop\python学习\接口_框架\suo_test',pattern='test_*.py')
        for  i in dis:
            suit.addTest(i)
    f=open(r'C:\Users\fang\Desktop\python学习\接口_框架\report\mm.html','wb')
    runner=HTMLTestRunner.HTMLTestRunner( stream=f,title='索赔测试报告',tester='方',description='结果如下')
    runner.run(suit)
    f.close()

