import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utils import logger
from common.base_page import BasePage
from element_infos.login_page import LoginPage
from element_infos.organization_page import OrganizationPage
from common.elements_data_utils import ElementDataUtils
#二级菜单权限页面元素

class AuthorityPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        # self.addGroup_button = {'element_name': '新增分组按钮',
        #                           'locator_type': 'xpath',
        #                           'locator_value':'//a[@href="/zentao4/www/group-create.html?onlybody=yes"]',
        #                           'timeout': 4}
        # #新增分组弹框页面元素
        # self.iframe = {'element_name':'分组弹框的iframe',
        #                           'locator_type':'xpath',
        #                           'locator_value':'//iframe[@id="iframe-triggerModal"]',
        #                           'timeout': 5 }
        #
        # self.groupName_inputbox = {'element_name':'分组名称输入框',
        #                           'locator_type':'xpath',
        #                           'locator_value':'//input[@id="name"]',
        #                           'timeout': 5 }
        # self.groupDescription_inputbox = {'element_name': '分组描述输入框',
        #                           'locator_type': 'xpath',
        #                           'locator_value': '//textarea[@id="desc"]',
        #                           'timeout': 4}
        # self.save_group_button = {'element_name': '保存按钮',
        #                           'locator_type': 'xpath',
        #                           'locator_value': '//button[@id="submit"]',
        #                           'timeout': 2}
        #编辑组
        # self.edit_group_button = {'element_name': '编辑组按钮',
        #                           'locator_type': 'xpath',
        #                           'locator_value': '//td[@title="%s"]/../td[5]/a[4]',
        #                           'timeout': 2}
        elements = ElementDataUtils('authority_page').get_element_info()
        self.addGroup_button=elements['addGroup_button']
        self.iframe=elements['iframe']
        self.groupName_inputbox=elements['groupName_inputbox']
        self.groupDescription_inputbox=elements['groupDescription_inputbox']
        self.save_group_button=elements['save_group_button']
        self.edit_group_button=elements['edit_group_button']




    def click_addGroup_button(self):
        self.click( self.addGroup_button )

    def input_groupName(self,groupName):
        self.input( self.groupName_inputbox ,groupName )

    def input_groupDescription(self,groupDescription):
        self.input( self.groupDescription_inputbox ,groupDescription )

    def switch_to_frame(self):
        self.switchToFrame(self.iframe)

    def click_save(self):
        self.click( self.save_group_button )

    def click_editGroup(self):
        self.edit_group_button['locator_value']=self.edit_group_button['locator_value']%'项目经理'
        self.click(self.edit_group_button)

if __name__=="__main__":
    # current_path = os.path.dirname(__file__)
    # driver_path = os.path.join(current_path,'webdriver/chromedriver.exe')
    # driver = webdriver.Chrome(executable_path=driver_path)
    driver = webdriver.Chrome()
    login_page =LoginPage(driver)
    login_page.open_url('http://106.53.50.202:8999/zentao4/www/user-login-L3plbnRhbzYvd3d3Lw==.html')
    login_page.set_browser_max()
    login_page.input_username('admin')
    login_page.input_password('admin@123')
    login_page.click_login()
    organization_page = OrganizationPage(driver)
    organization_page.click_organization_link()
    organization_page.click_authority_link()
    authority=AuthorityPage(driver)
    # authority.click_addGroup_button()
    authority.click_editGroup()
    authority.switch_to_frame()
    # authority.switch_to_frame()
    # authority.input_groupName('测试经理')
    # authority.input_groupDescription('给测试经理分组')
    # authority.click_save()




