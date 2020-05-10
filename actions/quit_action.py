from element_infos.login.login_page import LoginPage
from element_infos.main.main_page import MainPage

class QuitActions:
    def __init__(self,driver):
        self.main_page=MainPage(driver)

    def quit(self):
        self.main_page.click_username()
        self.main_page.click_quit_button()
        return LoginPage(self.main_page.driver)


# if __name__=='__main__':
    # driver=Browser().get_chrome_driver()
    # url = local_config.url
    # login_actions=LoginActions(driver)
    # BasePage(driver).open_url(url)
    # BasePage(driver).set_browser_max()
    # login_actions.default_login()
