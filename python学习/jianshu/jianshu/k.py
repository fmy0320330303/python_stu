# -*- coding: utf-8 -*- 

# @Time : 2019/4/8 下午2:22 

# @Author : 废柴 

# @Project: jianshu

# @FileName : k.py 

# @Software: PyCharm

# @Desc : ==============================================

# Life is Short I Use Python!!!                      ===

# If this runs wrong,don't ask me,I don't know why;  ===

# If this runs right,thank god,and I don't know why. ===

# Maybe the answer,my friend,is blowing in the wind. ===

# ======================================================

#
# def foo():
#     print("foo函数")
#
#
# def l():
#     foo()
#
#
# l()


# def biao(self, a1):
#     print("{}".format(a1))
#
#
# def tao(self):
#     biao("fk", 21)
#
# tao("t")

import  unittest
from selenium import webdriver
from time import sleep
class zhengjiang(unittest.TestCase):

    def  setUp(self):
        self.dr=webdriver.Firefox()
        self.dr.get('https://ai.taobao.com/')
    def test_01(self):
        self.dr.find_element_by_xpath('/html/body/div[1]/div/ul[1]/li[2]/div/a[1]').click()
        sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div[4]/div/div[5]/a[1]').click()
        sleep(2)
        self.dr.find_element_by_id('TPL_username_1').send_keys('qq1258153711')
        sleep(2)
        self.dr.find_element_by_id('TPL_password_1').send_keys('special1314...')
        sleep(2)
        self.dr.find_element_by_id('J_SubmitStatic').click()
        sleep(3)
        self.assertEqual(self.dr.title,'爱淘宝-淘宝网购物分享平台')

    def tearDown(self):
        self.dr.quit()
if __name__=='__mian__':
    unittest.main()
