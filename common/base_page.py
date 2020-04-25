import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.log_utils import logger

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver

    # 浏览器操作封装 -- > 二次封装
    def open_url(self,url):
        self.driver.get( url )
        logger.info('打开url地址 %s '% url )

    def set_browser_max(self):
        self.driver.maximize_window()
        logger.info('设置浏览器最大化')

    def set_browser_min(self):
        self.driver.minimize_window()
        logger.info('设置浏览器最小化')

    def refresh(self):
        self.driver.refresh()
        logger.info('浏览器刷新操作')

    def get_title(self):
        value = self.driver.title
        logger.info('获取网页标题，标题是%s'%value)
        return value

    def scrollIntoView(self):
        js_str='document.documentElement.scrollTop=100000;'# 浏览器滚动条下滑操作 js代码与浏览器兼容性
        self.driver.execute_script(js_str)
        time.sleep(2)
        logger.info('浏览器下滑到底部操作')

    def alert_accept(self):
        alert = self.driver.switch_to.alert  # 切换到JS弹窗
        alert.accept()  # 点击确定

    def alert_dismiss(self):
        alert = self.driver.switch_to.alert  # 切换到JS弹窗
        alert.dismiss()  # 点击确定
    #.....

    #元素操作封装
    # element_info = {'element_name':'用户名输入框','locator_type':'xpath','locator_value':'//input[@name="account"]','timeout': 5 }
    def find_element(self,element_info):
        locator_type_name = element_info['locator_type']
        locator_value_info = element_info['locator_value']
        locator_timeout = element_info['timeout']
        if locator_type_name == 'id':
            locator_type = By.ID
        if locator_type_name == 'name':
            locator_type = By.NAME
        elif locator_type_name == 'class':
            locator_type = By.CLASS_NAME
        elif locator_type_name == 'xpath':
            locator_type = By.XPATH
        element = WebDriverWait(self.driver,locator_timeout)\
            .until(lambda x:x.find_element(locator_type,locator_value_info))
        logger.info('[%s]元素识别成功'%element_info['element_name'])
        # element = WebDriverWait(self.driver, locator_timeout)\
        #     .until(EC.presence_of_element_located((locator_type, locator_value_info)))
        return element

    def click(self,element_info):
        element = self.find_element(element_info)
        element.click()
        logger.info('[%s]元素进行点击操作'%element_info['element_name'])



    def get_value(self,element_info,attribute):
        element = self.find_element(element_info)
        return element.get_attribute(attribute)
        logger.info('获取[%s]的属性值'%element_info['element_name'])

    def input(self,element_info,content):
        element = self.find_element(element_info)
        element.send_keys(content)
        logger.info('[%s]元素输入内容：%s' %(element_info['element_name'],content))

    def switchToFrame(self,element_info):
        element = self.find_element(element_info)
        self.driver.switch_to.frame(element)
        logger.info('[%s]iframe跳转'%element_info['element_name'])

    def clear(self,element_info):
        element = self.find_element(element_info)
        element.clear()
        logger.info('[%s]元素进行输入框清除操作'%element_info['element_name'])

    def select(self,element_info,content):
        element = self.find_element(element_info)
        Select(element).select_by_visible_text(content)
        logger.info('[%s]元素进行下拉选择操作'%element_info['element_name'])















