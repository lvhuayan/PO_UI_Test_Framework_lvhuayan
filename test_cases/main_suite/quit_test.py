import unittest
from common.base_page import BasePage
from common.config_utils import local_config
from common.browser import Browser
from actions.login_action import LoginActions
from actions.quit_action import  QuitActions
from common.selenium_base_page import SeleniumBasePage
from common.test_data_utils import TestDateUtils


class  QuitTest(SeleniumBasePage):
    quit_test_data = TestDateUtils('main_suite', 'QuitTest').convert_exceldata_to_testdata()

    def setUp(self) -> None:
        super().setUp()


    def tearDown(self) -> None:
        super().tearDown()


    def test_quit(self):
        loginaction=LoginActions(self.driver)
        test_function_data = self.quit_test_data['test_quit']
        main_page=loginaction.default_login()
        quit_actions=QuitActions(main_page.driver)
        login_page=quit_actions.quit()
        actual_result=login_page.get_title()
        self.assertEqual(actual_result.__contains__('用户登录'),test_function_data['expect_result'],'test_quit测试用例失败')

if __name__ == '__main__':
    unittest.main()


