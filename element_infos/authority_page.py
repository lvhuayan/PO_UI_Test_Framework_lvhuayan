import os
from selenium import webdriver
from common.elements_yaml_utils import get_element_from_yaml
from common.base_page import BasePage
from element_infos.login_page import LoginPage
from element_infos.user_page import OrganizationPage
from common.elements_data_utils import ElementDataUtils

current_path = os.path.dirname(__file__)
yaml_date_path = os.path.join(current_path, '../element_info_data/element_infos_authority_page.yaml')

#二级菜单权限页面元素
class AuthorityPage(BasePage):
    groupname_value=''
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

        # 方式一：excel文件做数据源
        # elements = ElementDataUtils('authority_page').get_element_info()

        # 方式二：yaml文件做数据源
        elements=get_element_from_yaml(yaml_date_path)
        self.addGroup_button=elements['addGroup_button']
        self.iframe=elements['iframe']
        self.groupName_inputbox=elements['groupName_inputbox']
        self.groupDescription_inputbox=elements['groupDescription_inputbox']
        self.save_group_button=elements['save_group_button']
        self.edit_group_button=elements['edit_group_button']
        self.delete_group_button=elements['delete_group_button']
        self.copy_group_button=elements['copy_group_button']

    def click_addGroup_button(self):
        self.click( self.addGroup_button )

    def input_groupName(self,groupName):
        self.input( self.groupName_inputbox ,groupName )

    def get_groupName(self,attribute):
        self.groupname_value=self.get_value(self.groupName_inputbox,attribute)

    def input_groupDescription(self,groupDescription):
        self.input( self.groupDescription_inputbox ,groupDescription )

    def switch_to_frame(self):
        self.switchToFrame(self.iframe)

    def click_save(self):
        self.click( self.save_group_button )

    def click_editGroup(self):
        self.edit_group_button['locator_value']=self.edit_group_button['locator_value']%self.groupname_value
        self.click(self.edit_group_button)

    def click_deleteGroup(self):
        self.delete_group_button['locator_value']=self.delete_group_button['locator_value']%self.groupname_value
        self.click(self.delete_group_button)

    def click_copy_group(self):
        self.copy_group_button['locator_value']=self.copy_group_button['locator_value']%self.groupname_value
        self.click(self.copy_group_button)

if __name__=="__main__":
    current_path = os.path.dirname(__file__)
    driver_path = os.path.join(current_path,'../webdriver/chromedriver.exe')
    driver = webdriver.Chrome(executable_path=driver_path)
    #登录
    login_page =LoginPage(driver)
    login_page.open_url('http://106.53.50.202:8999/zentao4/www/user-login-L3plbnRhbzYvd3d3Lw==.html')
    login_page.set_browser_max()
    login_page.input_username('admin')
    login_page.input_password('admin@123')
    login_page.click_login()
    #进入到权限页面
    organization_page = OrganizationPage(driver)
    organization_page.click_organization_link()
    organization_page.click_authority_link()
    authority=AuthorityPage(driver)
    #新增分组
    authority.click_addGroup_button()
    authority.switch_to_frame()
    authority.input_groupName('测试一部组4')
    authority.get_groupName('value')
    authority.input_groupDescription('测试一部组4')
    authority.click_save()
    authority.refresh()
    # # 复制分组
    # authority.scrollIntoView()
    # authority.click_copy_group()
    # authority.switch_to_frame()
    # authority.clear(authority.groupName_inputbox)
    # authority.input_groupName('测试一部组5')
    # authority.clear(authority.groupDescription_inputbox)
    # authority.input_groupDescription('测试一部组5')
    # authority.click_save()

    # #编辑分组
    # authority.refresh()
    # authority.scrollIntoView()
    # authority.click_editGroup()
    # authority.switch_to_frame()
    # authority.clear(authority.groupDescription_inputbox)
    # authority.input_groupDescription('测试一部组44')
    # authority.click_save()
    #删除分组
    authority.refresh()
    authority.scrollIntoView()
    authority.click_deleteGroup()
    authority.alert_accept()




