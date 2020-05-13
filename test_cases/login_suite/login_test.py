import unittest
from common.base_page import BasePage
from common.config_utils import local_config
from common.browser import Browser
from actions.login_action import LoginActions
from common.selenium_base_page import SeleniumBasePage
from common.test_data_utils import TestDateUtils


class LoginTest(SeleniumBasePage):

    login_test_data = TestDateUtils('login_suite', 'LoginTest').convert_exceldata_to_testdata()

    def setUp(self) -> None:
        '''
        该模块特有的setup内容，先要继承seleniumbasepage父类的setup然后在此处写特有内容
        :return:
        '''
        super().setUp()
        # print('该测试模块独有的setup内容需要先继承seleniumbasepage的setup方法然后再写独有的内容')


    def test_login_success(self):
        loginaction=LoginActions(self.driver)
        test_function_data =self.login_test_data['test_login_success']
        main_page=loginaction.login_success(test_function_data ['test_parameter'].get('username'),test_function_data ['test_parameter'].get('password'))
        actual_result=main_page.get_username()
        self.assertEqual(actual_result,'admin','test_login_success用例执行失败')

    def test_login_fail(self):
        loginaction=LoginActions(self.driver)
        test_function_data  = self.login_test_data['test_login_fail']
        actual_result=loginaction.login_fail(test_function_data ['test_parameter'].get('username'),test_function_data ['test_parameter'].get('password'))
        self.assertEqual(actual_result, '登录失败，请检查您的用户名或密码是否填写正确。', 'test_login_fail用例执行失败')


if __name__ == '__main__':
    unittest.main()


