import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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

    def scrollIntoView(self,element_info):
        element = self.find_element(element_info)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)
        time.sleep(2)
        logger.info('浏览器滚动到元素【%s】的位置'%element_info['element_name'])

    def scrollToBottom(self):
        self.driver.execute_script('document.documentElement.scrollTop=100000;')# 浏览器滚动条下滑操作到底部
        time.sleep(2)
        logger.info('浏览器下滑到底部操作')



    def clear(self,element_info):
        element = self.find_element(element_info)
        element.clear()
        logger.info('[%s]元素进行输入框清除操作'%element_info['element_name'])

    def select(self,element_info,content):
        element = self.find_element(element_info)
        Select(element).select_by_visible_text(content)
        logger.info('[%s]元素进行下拉选择操作'%element_info['element_name'])

    def switch_to_alert(self):
        alert=self.driver.switch_to.alert
        return alert

    def alert_sendkeys(self,content):
        self.switch_to_alert().sendkeys(content)  # 切换到JS弹窗，弹框中输入内容
        logger.info('切换到弹窗，输入内容%s' % content)

    def alert_accept(self):
        self.switch_to_alert().accept()  #切换到JS弹窗，点击确定
        logger.info('切换到弹窗，点击确定')

    def alert_dismiss(self):
        self.switch_to_alert().dismiss()  # 切换到JS弹窗，点击取消
        logger.info('切换到弹窗，点击取消')

    #selenium执行js代码
    def execute_script(self,js_str,element_info=None):
        if element_info:
            self.driver.execute_script(js_str)
        else:
            self.driver.execute_script(js_str,None)

    #移除属性
    def delete_element_attribute(self,element_info,attribute_name):
        element = self.find_element(element_info)
        self.execute_script('arguments[0].removeAttribute("%s");'%attribute_name,element)
        logger.info('[%s]元素进行属性移除操作'%element_info['element_name'])

    # 重新设置属性
    def set_element_attribute(self,element_info,attribute_name,attribute_value):
        element = self.find_element(element_info)
        self.execute_script('arguments[0].setAttribute("%s","%s");'%(attribute_name,attribute_value),element)
        logger.info('[%s]元素进行属性设置操作' % element_info['element_name'])

    def ctrl_v(self,element_info):
        element = self.find_element(element_info)
        element.send_keys(Keys.CONTROL,'v')
        logger.info('在元素[%s]上进行ctrl+v粘贴操作'%element_info['element_name'])

    def get_current_handle(self):
        handle = self.driver.current_window_handle
        return handle
        logger.info('获取当前窗口的句柄')


    def switch_to_handle(self,titleName):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.title.__contains__(titleName):
                break
        logger.info('切换句柄')



















