import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utils import logger
from common.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.username_inputbox = {'element_name':'用户名输入框',
                                  'locator_type':'xpath',
                                  'locator_value':'//input[@name="account"]',
                                  'timeout': 5 }
        self.password_inputbox = {'element_name': '密码输入框',
                                  'locator_type': 'xpath',
                                  'locator_value': '//input[@name="password"]',
                                  'timeout': 4}
        self.login_button = {'element_name': '登录按钮',
                                  'locator_type': 'xpath',
                                  'locator_value': '//button[@id="submit"]',
                                  'timeout': 2}


    def input_username(self,username): #方法 == 》控件的操作
        self.input( self.username_inputbox ,username )

    def input_password(self,password):
        self.input( self.password_inputbox ,password )

    def click_login(self):
        self.click( self.login_button )

# login_page =LoginPage()

if __name__=="__main__":
    # current_path = os.path.dirname(__file__)
    # driver_path = os.path.join(current_path,'../webdriver/chromedriver.exe')
    # driver = webdriver.Chrome(executable_path=driver_path)
    driver = webdriver.Chrome()
    login_page =LoginPage(driver)
    login_page.open_url('http://106.53.50.202:8999/zentao4/www/user-login-L3plbnRhbzYvd3d3Lw==.html')
    login_page.input_username('admin')
    login_page.input_password('admin@123')
    login_page.click_login()


