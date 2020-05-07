import os
from selenium import webdriver
from selenium.webdriver.common.by import By

from common.browser import Browser
from common.config_utils import local_config
from common.log_utils import logger
from common.base_page import BasePage
from common.elements_data_utils import  ElementDataUtils
from common.elements_yaml_utils import get_element_from_yaml

current_path = os.path.dirname(__file__)
yaml_date_path = os.path.join(current_path, '../element_info_data/element_infos_login_page.yaml')
class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        # self.username_inputbox = {'element_name':'用户名输入框',
        #                           'locator_type':'id',
        #                           'locator_value':'account]',
        #                           'timeout': 5 }
        # self.password_inputbox = {'element_name': '密码输入框',
        #                           'locator_type': 'name',
        #                           'locator_value': 'password',
        #                           'timeout': 4}
        # self.login_button = {'element_name': '登录按钮',
        #                           'locator_type': 'id',
        #                           'locator_value': 'submit',
        #                           'timeout': 2}
        # 方式一：excel文件做数据源
        elements=ElementDataUtils('login','login_page').get_element_info()

        # 方式二：yaml文件做数据源
        # elements=get_element_from_yaml(yaml_date_path)
        self.username_inputbox=elements['username_inputbox']
        self.password_inputbox = elements['password_inputbox']
        self.login_button = elements['login_button']


    def input_username(self,username): #方法 == 》控件的操作
        self.input( self.username_inputbox ,username )

    def input_password(self,password):
        self.input( self.password_inputbox ,password )

    def click_login(self):
        self.click( self.login_button )

    def get_login_fail_alert_content(self):
            return self.switch_to_alert()

# login_page =LoginPage()

if __name__=="__main__":
    # current_path = os.path.dirname(__file__)
    # driver_path = os.path.join(current_path,'../webdriver/chromedriver.exe')
    # driver = webdriver.Chrome(executable_path=driver_path)
    driver=Browser().get_chrome_driver()
    url = local_config.url
    # driver = webdriver.Chrome()
    login_page =LoginPage(driver)
    login_page.open_url(url)
    login_page.input_username('admin')
    login_page.input_password('admin@123')
    login_page.click_login()
    login_page.screenshot_asfile()



