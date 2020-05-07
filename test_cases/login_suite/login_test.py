import unittest
from common.base_page import BasePage
from common.config_utils import local_config
from common.browser import Browser
from actions.login_action import LoginActions

class LoginTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=Browser().get_driver()
        self.base_page=BasePage(self.driver)
        self.base_page.set_browser_max()
        self.base_page.open_url(local_config.url)

    def tearDown(self) -> None:
        self.base_page.close_tab()

    def test_login_success(self):
        login_action=LoginActions(self.base_page.driver)
        main_page=login_action.login_success('admin','admin@123')
        actual_result=main_page.get_username()
        self.assertEqual('admin','admin','test_login_success用例执行失败')

if __name__ == '__main__':
    unittest.main()


