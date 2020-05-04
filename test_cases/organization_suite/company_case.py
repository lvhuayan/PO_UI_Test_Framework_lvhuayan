import os
import  unittest
from selenium import  webdriver

from common.browser import Browser
from common.config_utils import local_config
from common.login import login
from common.logout import logout
from element_infos.user_page import OrganizationPage
from element_infos.company_page import CompanyPage


class CompanyCases(unittest.TestCase):
    driver =Browser().get_chrome_driver()
    url=local_config.url
    def setUp(self) -> None:
        login(self.driver,self.url,
              'admin','admin@123')
        # 跳转到公司页面
        organization_page = OrganizationPage(self.driver)
        organization_page.click_organization_link()  # 点击一级菜单组织链接
        organization_page.click_company_link() # 点击二级菜单公司链接

    def tearDown(self) -> None:
        logout(self.driver)

    def test_edit_company(self):
        # 编辑公司名称
        company_page=CompanyPage(self.driver)
        company_page.click_editCompany_button()
        company_page.switch_to_frame()
        company_page.clear_inputbox()
        company_page.input_companyName_inputbox('第四组Pro')
        company_page.click_save()
        company_page.refresh()

if __name__=='__main__':
    unittest.main()