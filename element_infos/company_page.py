import os
from selenium import webdriver
from common.elements_yaml_utils import get_element_from_yaml
from common.base_page import BasePage
from element_infos.login_page import LoginPage
from element_infos.user_page import OrganizationPage
from common.elements_data_utils import ElementDataUtils
#二级菜单公司页面元素
current_path = os.path.dirname(__file__)
yaml_date_path = os.path.join(current_path, '../element_info_data/element_infos_company_page.yaml')
class CompanyPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        # self.edit_company_button = {'element_name': '编辑公司按钮',
        #                           'locator_type': 'xpath',
        #                           'locator_value':'//a[@id="editCompany"]',
        #                           'timeout': 4}
        # self.iframe = {'element_name':'编辑公司的弹框的iframe',
        #                           'locator_type':'xpath',
        #                           'locator_value':'//iframe[@id="iframe-triggerModal"]',
        #                           'timeout': 5 }
        # #编辑公司弹框页面元素
        # self.companyName_inputbox = {'element_name':'公司名称输入框',
        #                           'locator_type':'xpath',
        #                           'locator_value':'//input[@id="name"]',
        #                           'timeout': 5 }
        # self.save_company_button = {'element_name':'保存公司修改按钮',
        #                           'locator_type':'xpath',
        #                           'locator_value':'//button[@id="submit"]',
        #                           'timeout': 5 }
        # 方式一：excel文件做数据源
        # elements = ElementDataUtils('company_page').get_element_info()

        # 方式二：yaml文件做数据源
        elements = get_element_from_yaml(yaml_date_path)
        self.edit_company_button=elements['edit_company_button']
        self.iframe=elements['iframe']
        self.companyName_inputbox=elements['companyName_inputbox']
        self.save_company_button=elements['save_company_button']

    def click_editCompany_button(self):
        self.click( self.edit_company_button )

    def input_companyName_inputbox(self,companyName):
        self.input( self.companyName_inputbox ,companyName )

    def switch_to_frame(self):
        self.switchToFrame(self.iframe)

    def clear_inputbox(self):
        self.clear( self.companyName_inputbox )

    def click_save(self):
        self.click( self.save_company_button )

if __name__=="__main__":
    current_path = os.path.dirname(__file__)
    driver_path = os.path.join(current_path,'../webdriver/chromedriver.exe')
    driver = webdriver.Chrome(executable_path=driver_path)
    login_page =LoginPage(driver)
    login_page.open_url('http://106.53.50.202:8999/zentao4/www/user-login-L3plbnRhbzYvd3d3Lw==.html')
    #登录系统
    login_page.set_browser_max()
    login_page.input_username('admin')
    login_page.input_password('admin@123')
    login_page.click_login()
    #跳转到公司页面
    organization_page = OrganizationPage(driver)
    organization_page.click_organization_link()
    organization_page.click_company_link()
    #编辑公司名称
    company_page=CompanyPage(driver)
    company_page.click_editCompany_button()
    company_page.switch_to_frame()
    company_page.clear_inputbox()
    company_page.input_companyName_inputbox('第四组Pro')
    company_page.click_save()




