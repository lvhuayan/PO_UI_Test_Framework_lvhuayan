import unittest
from common.base_page import BasePage
from common.config_utils import local_config
from common.browser import Browser
from actions.login_action import LoginActions
from common.selenium_base_page import SeleniumBasePage

class LoginTest(SeleniumBasePage):

    def setUp(self) -> None:
        '''
        该模块特有的setup内容，先要继承seleniumbasepage父类的setup然后在此处写特有内容
        :return:
        '''
        super().setUp()
        print('该测试模块独有的setup内容需要先继承seleniumbasepage的setup方法然后再写独有的内容')

    def test_login_success(self):
        loginaction=LoginActions(self.driver)
        main_page=loginaction.login_success('admin','admin@123')
        actual_result=main_page.get_username()
        self.assertEqual(actual_result,'admin','test_login_success用例执行失败')

    def test_login_fail(self):
        loginaction=LoginActions(self.driver)
        actual_result=loginaction.login_fail('admin','admin')
        self.assertEqual(actual_result, '登录失败，请检查您的用户名或密码是否填写正确。', 'test_login_fail用例执行失败')


if __name__ == '__main__':
    unittest.main()


