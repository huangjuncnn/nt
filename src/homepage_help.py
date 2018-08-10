from time import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from utils.log import logger
from selenium.webdriver.common.by import By

class homepage_help():
    def homepage_help(driver):
        driver.find_element_by_link_text('首页').click()
        sleep(1)
        js = 'window.scrollTo(100,1000);'     # 通过javascript设置浏览器窗口的滚动条位置
        driver.execute_script(js)
        # logger.info('开始点击费率了----------------------------------------------------')
        # locator_feilv = (By.LINK_TEXT,'费率')
        # driver.find_element(*locator_feilv).click()
        sleep(1)
        driver.find_element_by_link_text('新手帮助').click()
        sleep(0.5)
        driver.find_element_by_class_name('form-control').send_keys('NT101')
        driver.find_element_by_class_name('form-control').send_keys(Keys.ENTER)

        above = driver.find_element_by_link_text('157****4299')  # 定位要悬停的元素
        ActionChains(driver).move_to_element(above).perform()
        sleep(0.5)
        driver.find_element_by_link_text('安全退出').click()
        sleep(3)
