#！/bin/python
#-*- coding:utf-8 -*-
from appium import webdriver
from  time import sleep

import unittest

desired_caps={'platformName':'Android',
              'deviceName':'127.0.0.1:62001',
              'appPackage':'com.netease.cloudmusic',
              'appActivity':'.activity.LoadingActivity'}
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
sleep(15)
driver.find_element_by_id('com.netease.cloudmusic:id/qc').click()
sleep(5)
driver.find_element_by_id('com.netease.cloudmusic:id/ik').send_keys('17530132553')
sleep(5)
driver.find_element_by_id('com.netease.cloudmusic:id/ii').send_keys('fmy032.z')
sleep(5)
driver.find_element_by_id('com.netease.cloudmusic:id/qc').click()
sleep(5)
####断言
driver.find_element_by_id('com.netease.cloudmusic:id/qn').click()##点击抽屉菜单
sleep(5)
class wyy(unittest.TestCase):
    def test_1(self):
        a=driver.find_element_by_id('com.netease.cloudmusic:id/af4').text
        driver.assertEqual(a,'诌--沉浸')
    def tearDown(self):
        driver.quit()
if __name__=='__main__':
    unittest.main()