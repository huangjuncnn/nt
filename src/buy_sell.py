
from  time import *
from utils.log import logger
from selenium.webdriver.common.by import By



class buy_and_sell():
    def xianjiabuy(driver):
        driver.find_element_by_link_text('交易大厅').click()

        js = 'window.scrollTo(100,700);'   #通过javascript设置浏览器窗口的滚动条位置
        driver.execute_script(js)

        locator_xianjia = (By.CLASS_NAME,'btn-green')

        for i in range(2):
            driver.find_element_by_id('order_bid_price').send_keys('43888')
            driver.find_element_by_id('order_bid_origin_volume').send_keys('0.01')
            driver.find_element(*locator_xianjia).click()
            sleep(0.5)
        sleep(2)

    def xianjiasell(driver):
        for i in range(2):
            driver.find_element_by_id('order_ask_price').send_keys('43688')
            driver.find_element_by_id('order_ask_origin_volume').send_keys('0.01')
            driver.find_element_by_class_name('btn-orange').click()
            sleep(0.5)
        logger.info('pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp')
        # links = driver.find_elements(*locator_result)
        # for link in links:
        #     logger.info(link.text)

    def shijiabuy(driver):
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div[1]/ul/li[2]').click()

        for i in range(2):
            driver.find_element_by_id('order_bid_origin_volume').send_keys('0.01')
            driver.find_element_by_class_name('btn-green').click()
            sleep(0.5)
        sleep(2)
        # links = driver.find_elements(*locator_result)
        # for link in links:
        #     logger.info(link.text)