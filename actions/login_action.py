from common.base_page import BasePage
from common.browser import Browser
from common.config_utils import local_config
from element_infos.login.login_page import LoginPage
from element_infos.main.main_page import MainPage

class LoginActions():
    def __init__(self,driver):
        self.login_page=LoginPage(driver)

    def login_action(self,username,password):
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        self.login_page.click_login()

    def login_success(self,username,password):
        self.login_action(username,password)
        return MainPage(self.login_page.driver)

    def login_fail(self,username,password):
        self.login_action(username,password)
        return self.login_page.get_login_fail_alert_content()

    def default_login(self):
        return self.login_success(local_config.username,local_config.password)

    def login_by_cookie(self):
        pass

if __name__=='__main__':
    driver=Browser().get_chrome_driver()
    url = local_config.url
    login_actions=LoginActions(driver)
    BasePage(driver).open_url(url)
    BasePage(driver).set_browser_max()
    login_actions.default_login()
