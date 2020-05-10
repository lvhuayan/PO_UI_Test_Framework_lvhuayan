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
        self.base_page.implicitly_wait()
        self.base_page.open_url(local_config.url)


    def tearDown(self) -> None:
        self.base_page.close_tab()


    def test_login_success(self):
        loginaction=LoginActions(self.driver)
        main_page=loginaction.login_success('admin','admin@123')
        actual_result=main_page.get_username()
        self.assertEqual(actual_result,'admin','test_login_success用例执行失败')

    def test_login_fail(self):
        loginaction=LoginActions(self.driver)
        actual_result=loginaction.login_fail('admin','admin')
        print(actual_result)
        self.assertEqual(actual_result, '登录失败，请检查您的用户名或密码是否填写正确。', 'test_login_fail用例执行失败')


if __name__ == '__main__':
    unittest.main()


