import unittest
from common.base_page import BasePage
from common.config_utils import local_config
from common.browser import Browser
from actions.login_action import LoginActions
from actions.quit_action import  QuitActions


class LoginTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=Browser().get_driver()
        self.base_page=BasePage(self.driver)
        self.base_page.set_browser_max()
        self.base_page.implicitly_wait()
        self.base_page.open_url(local_config.url)


    def tearDown(self) -> None:
        self.base_page.close_tab()


    def test_quit(self):
        loginaction=LoginActions(self.driver)
        main_page=loginaction.default_login()
        quit_actions=QuitActions(main_page.driver)
        login_page=quit_actions.quit()
        actual_result=login_page.get_title()
        self.assertEqual(actual_result.__contains__('用户登录'),True,'test_quit测试用例失败')

if __name__ == '__main__':
    unittest.main()


