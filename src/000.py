from selenium import webdriver
from src.buy_sell import buy_and_sell
from src.user import user
from src.homepage_help import homepage_help
import logging
from HTMLTestRunner import HTMLTestRunner
import unittest

class Jiaoyisuo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()


    def test1(self):
        self.driver.get('http://192.168.50.247:3000/signin')
        self.driver.maximize_window()
        self.driver.find_element_by_id('identity_email').send_keys('15757164299')
        self.driver.find_element_by_id('identity_password').send_keys('a12345678')
        self.driver.find_element_by_name('commit').click()
        #
        user.user(self.driver)
        # user.work_list(self.driver)
        # user.Assets(self.driver)
        #
        # buy_and_sell.xianjiabuy(self.driver)
        # buy_and_sell.xianjiasell(self.driver)
        # buy_and_sell.shijiabuy(self.driver)
        # homepage_help.homepage_help(self.driver)


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Jiaoyisuo('test1'))

    # 定义报告存放路径
    fp = open('.result.html', 'wb')
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title='搜索测试报告',
                            description='用例执行情况')
    runner.run(testunit)  # 运行测试用例
    fp.close()  # 关闭报告文件
