import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utils import logger
from common.base_page import BasePage
from element_infos.login_page import LoginPage
from common.elements_data_utils import ElementDataUtils

#一级菜单 组织页面的元素
class UserPage(BasePage):
    username_value=''
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
        #
        #
        # self.addUser_button = {'element_name': '添加用户按钮',
        #                           'locator_type': 'xpath',
        #                           'locator_value':'//a[@href="/zentao4/www/user-create-0.html"]',
        #                           'timeout': 4}
        # self.batchAddUser_button = {'element_name': '批量添加用户按钮',
        #                           'locator_type': 'xpath',
        #                           'locator_value':'//a[@href="/zentao4/www/user-batchCreate-0.html"]',
        #                           'timeout': 4}
        # #添加用户页面的元素
        # self.belongToDepartment_select={'element_name': '所属部门选项',
        #                           'locator_type': 'xpath',
        #                           'locator_value':'//div[@id="dept_chosen"]',
        #                           'timeout': 4}
        # self.belongToDepartment_value={'element_name': '所属部门选项下拉值',
        #                           'locator_type': 'xpath',
        #                           'locator_value':'//div[@id="dept_chosen"]/div/ul/li[@title="/测试部"]',
        #                           'timeout': 4}
        # self.username_input={'element_name': '用户名输入框',
        #                           'locator_type': 'xpath',
        #                           'locator_value':'//input[@id="account"]',
        #                           'timeout': 4}
        # self.password_input={'element_name': '密码输入框',
        #                           'locator_type': 'xpath',
        #                           'locator_value':'//input[@id="password1"]',
        #                           'timeout': 4}
        # self.confirmPassword_input={'element_name': '确认密码输入框',
        #                           'locator_type': 'xpath',
        #                           'locator_value':'//input[@id="password2"]',
        #                           'timeout': 4}
        # self.realname_input={'element_name': '真实姓名输入框',
        #                           'locator_type': 'xpath',
        #                           'locator_value':'//input[@id="realname"]',
        #                           'timeout': 4}
        # self.position_input={'element_name': '职位',
        #                           'locator_type': 'xpath',
        #                           'locator_value':'//select[@id="role"]',
        #                           'timeout': 4}
        # self.sexman_radio={'element_name': '性别男',
        #                           'locator_type': 'xpath',
        #                           'locator_value':'//input[@id="genderm"]',
        #                           'timeout': 4}
        # self.sexfemal_radio={'element_name': '性别女',
        #                           'locator_type': 'xpath',
        #                           'locator_value':'//input[@id="genderf"]',
        #                           'timeout': 4}
        # self.verifyPassword_input={'element_name': '登录密码验证',
        #                           'locator_type': 'xpath',
        #                           'locator_value':'//input[@id="verifyPassword"]',
        #                           'timeout': 4}
        # self.save_user_button = {'element_name': '保存用户按钮',
        #                           'locator_type': 'xpath',
        #                           'locator_value': '//button[@id="submit"]',
        #                           'timeout': 4}
        # #编辑用户按钮
        # self.edit_user_button = {'element_name': '编辑用户按钮',
        #                           'locator_type': 'xpath',
        #                           'locator_value': '//a[@title="%s"]/../td[11]/a[1][@title="编辑用户"]',
        #                           'timeout': 4}
        # #删除用户按钮
        # self.delete_user_button = {'element_name': '删除用户按钮',
        #                           'locator_type': 'xpath',
        #                           'locator_value': '//a[@href="/zentao4/www/user-delete-2.html"]',
        #                           'timeout': 4}
        # self.iframe = {'element_name':'iframe',
        #                           'locator_type':'xpath',
        #                           'locator_value':'//iframe[@id="iframe-triggerModal"]',
        #                           'timeout': 5 }
        elements=ElementDataUtils('user_page').get_element_info()
        self.organization_link=elements['organization_link']
        self.user_link=elements['user_link']
        self.department_link=elements['department_link']
        self.authority_link=elements['authority_link']
        self.dynamic_link=elements['dynamic_link']
        self.company_link=elements['company_link']
        self.addUser_button=elements['addUser_button']
        self.batchAddUser_button=elements['batchAddUser_button']
        self.belongToDepartment_select=elements['belongToDepartment_select']
        self.belongToDepartment_value=elements['belongToDepartment_value']
        self.username_input=elements['username_input']
        self.password_input=elements['password_input']
        self.confirmPassword_input=elements['confirmPassword_input']
        self.realname_input=elements['realname_input']
        self.position_input=elements['position_input']
        self.verifyPassword_input=elements['verifyPassword_input']
        self.save_user_button=elements['save_user_button']
        self.edit_user_button=elements['edit_user_button']
        self.delete_user_button=elements['delete_user_button']
        self.iframe=elements['iframe']


    def click_organization_link(self):
        self.click( self.organization_link )

    def click_user_link(self):
        self.click( self.user_link )

    def click_department_link(self):
        self.click( self.department_link )

    def click_authority_link(self):
        self.click( self.authority_link )

    def click_company_link(self):
        self.click( self.company_link )

    def click_dynamic_link(self):
        self.click( self.dynamic_link )

    def click_addUser_button(self):
        self.click( self.addUser_button )

    def click_batchAddUser_button(self):
        self.click( self.batchAddUser_button )

    def click_addGroup_button(self):
        self.click( self.addGroup_button )

    def click_belongToDepartment_select(self):
        self.click( self.belongToDepartment_select )

    def click_belongToDepartment_value(self):
        self.click(self.belongToDepartment_value)

    def input_username(self,username):
        self.input(self.username_input,username)

    def get_username_value(self,attribute):
        self.username_value=self.get_value(self.username_input,attribute)

    def input_password(self,password):
        self.input(self.password_input,password)

    def input_confirmPassword(self,password):
        self.input(self.confirmPassword_input,password)

    def input_realname(self,realname):
        self.input(self.realname_input,realname)

    def click_position(self):
        self.click(self.position_input)

    def select_position_value(self,positionName):
        self.select(self.position_input,positionName)

    def click_sexman(self):
        self.click(self.sexman_radio)

    def click_sexfemal(self):
        self.click(self.sexfemal_radio)

    def input_verifyPassword(self,verifyPassword):
        self.input(self.verifyPassword_input,verifyPassword)

    def click_save(self):
        self.click(self.save_user_button)

    def clear_inputbox(self):
        self.clear( self.realname_input )

    def click_editUser_button(self):
        self.edit_user_button['locator_value']=self.edit_user_button['locator_value']%self.username_value
        self.click( self.edit_user_button )

    def click_deleteUser_button(self):
        self.click( self.delete_user_button )

    def scroll_IntoView(self):
        self.scrollIntoView(self.save_user_button)
    def switch_to_frame(self):
        self.switchToFrame(self.iframe)


if __name__=="__main__":
    driver = webdriver.Chrome()
    login_page =LoginPage(driver)
    login_page.open_url('http://106.53.50.202:8999/zentao4/www/user-login-L3plbnRhbzYvd3d3Lw==.html')
    login_page.set_browser_max()
    login_page.input_username('admin')
    login_page.input_password('admin@123')
    login_page.click_login()

    user_page=UserPage(driver)
    user_page.click_organization_link() #点击一级菜单组织链接
    user_page.click_user_link()#点击二级菜单用户链接
    # user_page.click_department_link()#点击二级菜单部门链接
    # user_page.click_authority_link()#点击二级菜单权限链接
    # user_page.click_company_link()#点击二级菜单公司链接
    # user_page.click_dynamic_link()#点击二级菜单动态链接

    user_page.click_addUser_button()
    user_page.click_belongToDepartment_select()
    user_page.click_belongToDepartment_value()
    user_page.input_username('lvhuayan')
    user_page.get_username_value('value')
    user_page.input_password('lvhuayan@123')
    user_page.input_confirmPassword('lvhuayan@123')
    user_page.input_realname('吕华艳')
    user_page.click_position()
    user_page.select_position_value('测试主管')
    user_page.input_verifyPassword('admin@123')
    user_page.click_save()
#编辑用户
    user_page.click_editUser_button()
    user_page.clear_inputbox()
    user_page.input_realname('吕华艳艳')
    user_page.scroll_IntoView()

    user_page.click_save()







