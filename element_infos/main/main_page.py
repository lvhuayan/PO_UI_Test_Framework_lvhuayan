
from common.base_page import BasePage
from common.elements_data_utils import ElementDataUtils
from common.browser import Browser

class MainPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        # 方式一：excel文件做数据源
        elements = ElementDataUtils('main', 'main_page').get_element_info()
        self.myzone_link=elements['myzone_link']
        self.user_menu = elements['user_menu']
        self.quit_button = elements['quit_button']


    def goto_myzone(self):  # 进入我的地盘菜单
        self.click(self.myzone_link)

    def get_username(self):
        return self.get_text(self.user_menu)

    def click_username(self):
        self.click(self.user_menu)

    def click_quit_button(self):
        self.click(self.quit_button)


if __name__=="__main__":
    driver=Browser().get_driver()
    # driver.get('http://106.53.50.202:8999/zentao4/www/user-login.html')
    # main_page=LoginActions(driver).default_login()
    # value= main_page.get_username()
    # print(value)
    main=MainPage(driver)



