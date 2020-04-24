import  unittest
from selenium import  webdriver
from common.base_page import BasePage
from common.login import login
from element_infos.login_page import LoginPage
from element_infos.user_page import OrganizationPage
from element_infos.company_page import CompanyPage


class CompanyCases(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        login(self.driver,'http://106.53.50.202:8999/zentao4/www/user-login-L3plbnRhbzYvd3d3Lw==.html',
              'admin','admin@123')

    def tearDown(self) -> None:
         # self.driver.quit()
        pass


    def test_edit_company(self):
        organization_page = OrganizationPage(self.driver)
        organization_page.click_organization_link()  # 点击一级菜单组织链接
        organization_page.click_company_link() # 点击二级菜单公司链接
        company_page=CompanyPage(self.driver)
        company_page.click_editCompany_button()
        company_page.switch_to_frame()
        company_page.clear_inputbox()
        company_page.input_companyName_inputbox('第四组Pro')
        company_page.click_save()

if __name__=='__main__':
    unittest.main()