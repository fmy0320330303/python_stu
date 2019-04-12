#！/bin/python
#-*- coding:utf-8 -*-
# from selenium  import webdriver
# from time import sleep
# #####定义使用什么浏览器
# dr=webdriver.Firefox()
###设置浏览器的大小
# dr.set_window_size(500,500)
# sleep(2)
# #####设置浏览器的位置
# dr.set_window_position(800,400)
# sleep(2)
####设置浏览器的最大化
# dr.maximize_window()
#####设置浏览器最小化
# dr.minimize_window()
#####打开网址
# dr.get('https://www.baidu.com')
# sleep(2)
# dr.get('https://www.jd.com')
# sleep(2)
# #####回退上一步
# dr.back()
# sleep(2)
# #####前进
# dr.forward()
# sleep(2)
# #####获取网址的标题
# print(dr.title)
# ####获取打开的网址
# print(dr.current_url)
#######定位（核心）
###1，id来定位，标签的id属性
# dr.find_element_by_id('kw').send_keys('lol')
# sleep(2)
# dr.find_element_by_id('su').click()######点击按钮的动作
# sleep(2)
###2，class_name来定位，标签的class属性
# dr.find_element_by_class_name('s_ipt').send_keys('dsahdljaldwajdlnvfefowodwwqcd')
# dr.find_element_by_class_name('bg s_btn').click()
###3，通过标签上的name定位，标签的name属性
# dr.find_element_by_name('wd').send_keys('akdjoisajdoisajdaijdaiqwdwdwqd')
# sleep(2)
# dr.find_element_by_id('su').click()
###4,通过标签的文本来定位
#dr.find_element_by_link_text('hao123').click()
###5,partial_link_text定位，标签的模糊文本定位
#dr.find_element_by_partial_link_text('hao').click()
####6，tag_name,通过标签名称定位,是最不唯一的定位，通常定位一组数据
#dr.find_elements_by_tag_name('input')
###7，css_selector定位，css来定位
# dr.find_element_by_css_selector('#kw').send_keys('dahdsahdksajdlsajdkjciwsal')
# sleep(2)
# dr.find_element_by_css_selector('#su').click()
###8，xpath定位，路径定位，路径标记语言，，，xml：可扩展性标记语言
# dr.find_element_by_xpath('//*[@id="kw"]').send_keys('lol')
# dr.find_element_by_xpath('//*[@id="su"]').click()
###id>css>xpath>name>class_name>>>>>>>>>定位的优先级

####关闭浏览器，断开连接
#dr.quit()
# ####关闭浏览器，不断开链接
# ###dr.close()
# from selenium  import webdriver
# from time import sleep
# dr=webdriver.Firefox()
# dr.maximize_window()
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.action_chains import ActionChains
# dr.get('https://mail.qq.com/cgi-bin/loginpage')
# sleep(2)
######处理框架     iframe是一个窗口
# dr.switch_to.frame('login_frame')###里面可以写框架的id和name，或者先定位到框架
# sleep(2)
# dr.find_element_by_id('switcher_plogin').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="u"]').send_keys('1562065932')
# sleep(2)
# dr.find_element_by_css_selector('#p').send_keys('fmy032.z')
# sleep(2)
# dr.find_element_by_id('login_button').click()
# dr.get('https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index')
###定位一组数据
# wd=dr.find_elements_by_class_name('mnav')
# ####层级定位,遇到复杂的元素定位
# wd=dr.find_element_by_tag_name('')
# wd=dr.find_element_by_id('searchHotelLevelSelect').find_elements_by_tag_name('option')
# sleep(2)
# for i in wd:
#     i.click()
#     sleep(2)
#####模拟动作
##send_keys()输入
##click（）点击
##text  获取定位到的元素文本
##clear()  清空定位到的元素数据
#dr.get('https://www.douban.com')
######处理框架     iframe是一个窗口,切换到某个框架
# dr.switch_to.frame('login_frame')###里面可以写框架的id和name，或者先定位到框架
# sleep(2)
#####回到最开始的框架，即为初始的框架
# dr.switch_to.default_content()
# ####回到父框架中
# dr.switch_to.parent_frame()
#dr.find_element_by_xpath('/html/body/div[1]/div[1]/ul/li[1]/a').click()
####处理浏览器窗口
###获取当前窗口的字符串(句柄)
# print(dr.current_window_handle)
# ######获取所有窗口的句柄
# qq=dr.window_handles
# dr.switch_to.window(qq[-1])
# dr.title
###模拟鼠标的操作
#####把鼠标移到元素的中心点
# dr.get('https://www.jd.com')
# sleep(2)
# w=dr.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div[1]/div/ul').find_elements_by_tag_name('li')
# for i in w:
#     ##控制鼠标移动到元素的位置上                 执行
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(2)
# # dr.quit()
###登陆京东，并滑动窗口
# dr.find_element_by_xpath('/html/body/div[1]/div[2]/div/ul[2]/li[1]/a[1]').click()
# sleep(2)
# dr.find_element_by_css_selector('html body div#content div.login-wrap div.w div.login-form div.login-tab.login-tab-r a').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="loginname"]').send_keys(18236549823)
# sleep(2)
# dr.find_element_by_xpath('//*[@id="nloginpwd"]').send_keys('special1314...')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="loginsubmit"]').click()
# sleep(2)
# ##drag_and_drop(其实位置，结束位置)
# # drag_and_drop_by_offset(起始位置，x轴坐标，y轴坐标)
# start = dr.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div[3]')
# ActionChains(dr).drag_and_drop_by_offset(start,60,0).perform()
# sleep(2)
# dr.get('http://www.lwfree.cn/yurenjie/yuerenjie1.html')
# sleep(2)
# ###切换到弹出窗
# ww=dr.switch_to.alert
# ##获取弹出框的内容
# while True:
#     print(ww.text)
#     ###点击确定
#     ww.accept()
#     sleep(2)
# # ##点击取消
# ww.dismiss
# ##输入
# ww.send_kes('内容')
# sleep(2)
####处理页面滚动条   javaScript语句
# js="var q=documentElement.scrollTop=1000"
# ####执行javaScript语句
# dr.execute_script(js)
###强制等待
# sleep(2)
###智能等待，设置一个最大等待时间，遇到某个元素出现，就不会继续等待
# unit=ui.WebDriverWait(dr,10)
###直到遇到的出现，就不等待了
# unit.until(lambda dr:dr.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[5]/ul[1]/li[1]/a'))
# print('123')
# w=dr.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[5]/ul[1]/li[3]/a')
# a=w.get_attribute('href')
# print(a)
########测试扣扣空间登陆

from selenium import webdriver
import unittest
from time import sleep
import xlrd
from ddt import ddt,unpack,data
class Lonin(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Firefox()
        self.dr.maximize_window()
        self.dr.get('https://www.baidu.com')
        self.dr.find_element_by_xpath('//*[@id="kw"]').send_keys('扣扣空间登陆')
        self.dr.find_element_by_xpath('//*[@id="su"]').click()
        sleep(3)
        self.dr.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div[3]/div[1]/h3/a/em').click()
        sleep(2)
        qq=self.dr.window_handles
        self.dr.switch_to.window(qq[-1])
        sleep(2)
        self.dr.switch_to.frame('login_frame')
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
        sleep(2)

    def test_shuru(self):
        self.dr.find_element_by_xpath('//*[@id="u"]').send_keys('1562065932')
        sleep(2)
        self.dr.find_element_by_css_selector('#p').send_keys('fmy032.z')
        sleep(2)
        self.dr.find_element_by_id('login_button').click()
        sleep(6)
        self.assertEqual(self.dr.title,'洛夜 [http://1562065932.qzone.qq.com]')


    def test_shuru2(self):

        self.dr.find_element_by_xpath('//*[@id="u"]').clear()
        self.dr.find_element_by_xpath('//*[@id="u"]').send_keys('156065932')
        sleep(2)
        self.dr.find_element_by_css_selector('#p').send_keys('fmy032.z')
        sleep(2)
        self.dr.find_element_by_id('login_button').click()
        sleep(6)
        self.assertNotEqual(self.dr.title, '洛夜 [http://1562065932.qzone.qq.com]')

    def tearDown(self):
        self.dr.quit()


# start=dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
# ActionChains(dr).drag_and_drop_by_offset(start,60,0).perform()
if __name__=='__main__':
    unittest.main()
