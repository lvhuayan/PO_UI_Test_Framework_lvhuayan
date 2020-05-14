import os
from common.base_page import BasePage
from element_infos.login.login_page import LoginPage
from common.elements_data_utils import ElementDataUtils
from common.browser import Browser
from common.config_utils import local_config

#一级菜单 组织页面的元素
current_path = os.path.dirname(__file__)
yaml_date_path = os.path.join(current_path, '../element_info_data/element_infos_organization_page.yaml')

class OrganizationPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        # self.organization_link = {'element_name':'一级菜单-组织链接',
        #                           'locator_type':'xpath',
        #                           'locator_value':'//li[@data-id="company"]',
        #                           'timeout': 5 }
        # self.user_link = {'element_name':'二级菜单栏-用户链接',
        #                           'locator_type':'xpath',
        #                           'locator_value':'//li[@data-id="browseUser"]',
        #                           'timeout': 5 }
        # self.department_link = {'element_name':'二级菜单栏-部门链接',
        #                           'locator_type':'xpath',
        #                           'locator_value':'//li[@data-id="dept"]',
        #                           'timeout': 5 }
        # self.authority_link = {'element_name':'二级菜单栏-权限链接',
        #                           'locator_type':'xpath',
        #                           'locator_value':'//li[@data-id="browseGroup"]',
        #                           'timeout': 5 }
        # self.dynamic_link = {'element_name':'二级菜单栏-动态链接',
        #                           'locator_type':'xpath',
        #                           'locator_value':'//li[@data-id="dynamic"]',
        #                           'timeout': 5 }
        # self.company_link = {'element_name':'二级菜单栏-公司链接',
        #                           'locator_type':'xpath',
        #                           'locator_value':'//li[@data-id="view"]',
        #                           'timeout': 5 }
        # 方式一：excel文件做数据源
        elements=ElementDataUtils('organization','organization_page').get_element_info()

        # 方式二：yaml文件做数据源
        # elements = get_element_from_yaml(yaml_date_path)
        self.organization_link=elements['organization_link']
        self.user_link=elements['user_link']
        self.department_link=elements['department_link']
        self.authority_link=elements['authority_link']
        self.dynamic_link=elements['dynamic_link']
        self.company_link=elements['company_link']

    def click_organization_link(self):
        self.click(self.organization_link)

    def click_user_link(self):
        self.click(self.user_link)

    def click_department_link(self):
        self.click(self.department_link)

    def click_authority_link(self):
        self.click(self.authority_link)

    def click_company_link(self):
        self.click(self.company_link)

    def click_dynamic_link(self):
        self.click(self.dynamic_link)

if __name__=="__main__":
    # current_path = os.path.dirname(__file__)
    # driver_path = os.path.join(current_path,'../webdriver/chromedriver.exe')
    # driver = webdriver.Chrome(executable_path=driver_path)

    driver = Browser().get_chrome_driver()
    url = local_config.url

    login_page =LoginPage(driver)
    # login_page.open_url('http://106.53.50.202:8999/zentao4/www/user-login-L3plbnRhbzYvd3d3Lw==.html')
    login_page.open_url(url)
    login_page.set_browser_max()
    #登录
    login_page.input_username('admin')
    login_page.input_password('admin@123')
    login_page.click_login()
    #点击链接查看是否正常
    organization_page=OrganizationPage(driver)
    organization_page.click_organization_link() #点击一级菜单组织链接
    organization_page.click_user_link()#点击二级菜单用户链接
    organization_page.click_department_link()#点击二级菜单部门链接
    organization_page.click_authority_link()#点击二级菜单权限链接
    organization_page.click_company_link()#点击二级菜单公司链接
    organization_page.click_dynamic_link()#点击二级菜单动态链接