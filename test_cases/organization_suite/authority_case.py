import  unittest
from selenium import  webdriver
from common.base_page import BasePage
from common.login import login
from element_infos.login_page import LoginPage
from element_infos.organization_page import OrganizationPage
from element_infos.authority_page import AuthorityPage


class UserCases(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        login(self.driver,'http://106.53.50.202:8999/zentao4/www/user-login-L3plbnRhbzYvd3d3Lw==.html',
              'admin','admin@123')

    def tearDown(self) -> None:
        self.driver.quit()
        pass
    #添加分组
    # def test_add_goup(self):
    #     organization_page = OrganizationPage(self.driver)
    #     organization_page.click_organization_link()  # 点击一级菜单组织链接
    #     organization_page.click_authority_link()  # 点击二级菜单用户链接
    #     authority_page=AuthorityPage(self.driver)
    #     authority_page.click_addGroup_button()
    #     authority_page.switch_to_frame()
    #     authority_page.input_groupName('测试一主管')
    #     authority_page.input_groupDescription('测试一主管')
    #     authority_page.click_save()
    #编辑分组
    def test_add_goup(self):
        organization_page = OrganizationPage(self.driver)
        organization_page.click_organization_link()  # 点击一级菜单组织链接
        organization_page.click_authority_link()  # 点击二级菜单用户链接
        authority_page=AuthorityPage(self.driver)
        authority_page.click_editGroup()# 点击编辑组按钮
        authority_page.switch_to_frame()



if __name__=='__main__':
    unittest.main()