import  unittest
from selenium import  webdriver
from common.base_page import BasePage
from common.login import login
from element_infos.login_page import LoginPage
from element_infos.user_page import OrganizationPage


class UserCases(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        login(self.driver,'http://106.53.50.202:8999/zentao4/www/user-login-L3plbnRhbzYvd3d3Lw==.html',
              'admin','admin@123')

    def tearDown(self) -> None:
        self.driver.quit()
    #验证链接可点击
    def test1_link_isNormal(self):
        organization_page = OrganizationPage(self.driver)
        organization_page.click_organization_link()  # 点击一级菜单组织链接
        organization_page.click_user_link()  # 点击二级菜单用户链接
        organization_page.click_department_link()#点击二级菜单部门链接
        organization_page.click_authority_link()#点击二级菜单权限链接
        organization_page.click_company_link()#点击二级菜单公司链接
        organization_page.click_dynamic_link()#点击二级菜单动态链接

    #添加新用户
    def test_addUser(self):
        organization_page = OrganizationPage(self.driver)
        organization_page.click_organization_link()  # 点击一级菜单组织链接
        organization_page.click_user_link()  # 点击二级菜单用户链接
        organization_page.click_addUser_button()
        organization_page.click_belongToDepartment_select()
        organization_page.click_belongToDepartment_value()
        organization_page.input_username('lvhuayan')
        organization_page.input_password('lvhuayan@123')
        organization_page.input_confirmPassword('lvhuayan@123')
        organization_page.input_realname('吕华艳')
        organization_page.click_position()
        organization_page.select_position_value('测试主管')
        organization_page.input_verifyPassword('admin@123')
        organization_page.click_save()

    # #添加已存在的用户
    def test2_addExistsUser(self):
        organization_page = OrganizationPage(self.driver)
        organization_page.click_organization_link()  # 点击一级菜单组织链接
        organization_page.click_user_link()  # 点击二级菜单用户链接
        organization_page.click_addUser_button()
        organization_page.click_belongToDepartment_select()
        organization_page.click_belongToDepartment_value()
        organization_page.input_username('lvhuayan')
        organization_page.input_password('lvhuayan@123')
        organization_page.input_confirmPassword('lvhuayan@123')
        organization_page.input_realname('吕华艳')
        organization_page.click_position()
        organization_page.select_position_value('测试主管')
        organization_page.input_verifyPassword('admin@123')
        organization_page.click_save()

    # #编辑用户
    def test_edit_user(self):
        organization_page = OrganizationPage(self.driver)
        organization_page.click_organization_link()  # 点击一级菜单组织链接
        organization_page.click_user_link()  # 点击二级菜单用户链接
        organization_page.click_editUser_button()
        organization_page.clear_inputbox()
        organization_page.input_realname('吕晓晓')
        organization_page.scroll_IntoView()
        organization_page.click_save()
    #删除用户
    def test_delete_user(self):
        organization_page = OrganizationPage(self.driver)
        organization_page.click_organization_link()  # 点击一级菜单组织链接
        organization_page.click_user_link()  # 点击二级菜单用户链接
        organization_page.click_deleteUser_button()
        organization_page.switch_to_frame()
        organization_page.input_verifyPassword('admin@123')
        organization_page.click_save()

if __name__=='__main__':
    unittest.main()