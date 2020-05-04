import  unittest
import os
from selenium import  webdriver
from common.base_page import BasePage
from common.login import login
from common.logout import logout
from element_infos.login_page import LoginPage
from element_infos.user_page import UserPage
from element_infos.user_page import OrganizationPage
from common.browser import Browser
from common.config_utils import local_config

class UserCases(unittest.TestCase):
    driver =Browser().get_chrome_driver()
    url=local_config.url
    def setUp(self) -> None:
        login(self.driver,self.url,
              'admin','admin@123')
        #跳转到用户页面
        organization_page = OrganizationPage(self.driver)
        organization_page.click_organization_link()  # 点击一级菜单组织链接
        organization_page.click_user_link()  # 点击二级菜单用户链接

    def tearDown(self) -> None:
        logout(self.driver)
    #验证链接可点击
    def test_link_isNormal(self):
        organization_page = OrganizationPage(self.driver)
        organization_page.click_organization_link()  # 点击一级菜单组织链接
        organization_page.click_user_link()  # 点击二级菜单用户链接
        organization_page.click_department_link()#点击二级菜单部门链接
        organization_page.click_authority_link()#点击二级菜单权限链接
        organization_page.click_company_link()#点击二级菜单公司链接
        organization_page.click_dynamic_link()#点击二级菜单动态链接

    #添加新用户
    def test_addUser(self):
        #添加用户
        user_page=UserPage(self.driver)
        user_page.click_addUser_button()
        user_page.click_belongToDepartment_select()
        user_page.click_belongToDepartment_value()
        user_page.input_username('lisa3')
        user_page.input_password('lisa@123')
        user_page.input_confirmPassword('lisa@123')
        user_page.input_realname('李莎')
        user_page.click_position()
        user_page.select_position_value('测试主管')
        user_page.input_verifyPassword('admin@123')
        user_page.click_save()

    #添加已存在的用户
    def test_addExistsUser(self):
        #添加用户
        user_page=UserPage(self.driver)
        user_page.click_addUser_button()
        user_page.click_belongToDepartment_select()
        user_page.click_belongToDepartment_value()
        user_page.input_username('lisa3')
        user_page.input_password('lisa@123')
        user_page.input_confirmPassword('lisa@123')
        user_page.input_realname('李莎')
        user_page.click_position()
        user_page.select_position_value('测试主管')
        user_page.input_verifyPassword('admin@123')
        user_page.click_save()
        user_page.refresh()

    #新增用户-编辑用户
    def test_edit_user(self):
        user_page=UserPage(self.driver)
        user_page.click_addUser_button()
        user_page.click_belongToDepartment_select()
        user_page.click_belongToDepartment_value()
        user_page.input_username('lisa4')
        user_page.get_username_value('value')
        user_page.input_password('lisa@123')
        user_page.input_confirmPassword('lisa@123')
        user_page.input_realname('李莎')
        user_page.click_position()
        user_page.select_position_value('测试主管')
        user_page.input_verifyPassword('admin@123')
        user_page.click_save()
        #编辑用户
        user_page.click_editUser_button()
        user_page.clear_realname_inputbox()
        user_page.input_realname('你妹')
        user_page.scroll_Into_View()
        user_page.input_verifyPassword('admin@123')
        user_page.click_save()

    #新增-编辑-删除用户
    def test_delete_user(self):
        #新增用户
        user_page=UserPage(self.driver)
        user_page.click_addUser_button()
        user_page.click_belongToDepartment_select()
        user_page.click_belongToDepartment_value()
        user_page.input_username('lisa5')
        user_page.get_username_value('value')
        user_page.input_password('lisa@123')
        user_page.input_confirmPassword('lisa@123')
        user_page.input_realname('李莎')
        user_page.click_position()
        user_page.select_position_value('测试主管')
        user_page.input_verifyPassword('admin@123')
        user_page.click_save()
        #编辑用户
        user_page.click_editUser_button()
        user_page.clear_realname_inputbox()
        user_page.input_realname('李梅')
        user_page.scroll_Into_View()
        user_page.input_verifyPassword('admin@123')
        user_page.click_save()
        #删除用户
        user_page.refresh()
        user_page.click_deleteUser_button()
        user_page.switch_to_frame()
        user_page.input_verifyPassword('admin@123')
        user_page.click_save()

if __name__=='__main__':
    unittest.main()