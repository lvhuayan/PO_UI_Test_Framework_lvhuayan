import os
from common.base_page import BasePage
from element_infos.login.login_page import LoginPage
from common.elements_data_utils import  ElementDataUtils
from common.browser import Browser
from common.config_utils import local_config

current_path = os.path.dirname(__file__)
yaml_date_path = os.path.join(current_path, '../element_info_data/element_infos_logout_page.yaml')
class LogoutPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        # self.username_link = {'element_name':'登录用户名',
        #                           'locator_type':'xpath',
        #                           'locator_value':'//span[@class="user-name"]',
        #                           'timeout': 5 }

        # self.click_logout = {'element_name': '退出按钮',
        #                           'locator_type': 'xpath',
        #                           'locator_value': '//a[contains(@href,"user-logout.html")]',
        #                           'timeout': 4}
        # 方式一：excel文件做数据源
        elements=ElementDataUtils('logout_page').get_element_info()

        # 方式二：yaml文件做数据源
        # elements = get_element_from_yaml(yaml_date_path)
        self.username_link=elements['username_link']
        self.logout_button = elements['logout_button']

    def click_username(self):
        self.click( self.username_link )

    def click_logout(self):
        self.click( self.logout_button )

if __name__=="__main__":
    # current_path = os.path.dirname(__file__)
    # driver_path = os.path.join(current_path,'../webdriver/chromedriver.exe')
    # driver = webdriver.Chrome(executable_path=driver_path)
    driver=Browser().get_chrome_driver()
    url = local_config.url
    login_page =LoginPage(driver)
    # login_page.open_url('http://106.53.50.202:8999/zentao4/www/user-login-L3plbnRhbzYvd3d3Lw==.html')
    login_page.open_url(url)
    login_page.set_browser_max()
    login_page.input_username('admin')
    login_page.input_password('admin@123')
    login_page.click_login()
    login_page.refresh()
    #退出
    logout_page=LogoutPage(driver)
    logout_page.click_username()
    logout_page.click_logout()




