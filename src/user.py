from time import *
from selenium.webdriver.common.action_chains import ActionChains
import win32comext
import win32com

class user():
    def user(driver):
        driver.find_element_by_link_text('实名认证').click()
        sleep(0.5)
        driver.find_element_by_link_text('邀请朋友').click()
        sleep(0.5)
        driver.find_element_by_link_text('我的工单').click()
        sleep(0.5)
        # driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[2]/div[3]/ul/li[2]/a/span[1]').click()
        # sleep(2)
        driver.find_element_by_link_text('历史成交').click()
        sleep(1)
        above = driver.find_element_by_link_text('157****4299')                                                          # 定位要悬停的元素
        ActionChains(driver).move_to_element(above).perform()
        sleep(0.5)
        driver.find_element_by_link_text('我的工单').click()
        sleep(0.5)

    def work_list(driver):
        driver.find_element_by_link_text('新建工单').click()
        driver.find_element_by_class_name('foot').click()
        driver.find_element_by_id('ticket_title').send_keys('请问你在吗')
        driver.find_element_by_id('ticket_content').send_keys('你好我在')
        # driver.find_element_by_name('commit').click()
        # sleep(1)

    def Assets(driver):
        driver.find_element_by_link_text('资产余额').click()
        sleep(1)
        driver.find_element_by_id('deposit_sum').send_keys('50000')  # 充值
        driver.find_element_by_id('deposit_fund_uid').send_keys('54654432453434')
        sleep(1)
        driver.find_element_by_name('commit').click()
        upload = driver.find_element_by_xpath('html/body/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/ui-view/ui-view[1]/ng-include[1]/section[1]/form/div[2]/div[1]/div[7]/span[2]/div/p[1]/button')
        upload.send_keys('d:\\11.jpg')
        sleep(10)
        print (upload.get_attribute('value'))


        driver.find_element_by_xpath('html/body/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/ui-view/ui-view[1]/ng-include[1]/section[1]/form/div[2]/div[1]/div[8]/span[2]/button[1]').click()
        sleep(3)

        driver.find_element_by_link_text('提现').click()
        sleep(1)