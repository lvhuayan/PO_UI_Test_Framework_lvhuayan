import os
import  unittest
from selenium import  webdriver

from common.browser import Browser
from common.config_utils import local_config
from common.login import login
from common.logout import logout
from element_infos.user_page import OrganizationPage
from element_infos.authority_page import AuthorityPage

current_path = os.path.dirname(__file__)
yaml_date_path = os.path.join(current_path, '../element_info_data/element_infos_login_page.yaml')

class UserCases(unittest.TestCase):
    driver =Browser().get_chrome_driver()
    url=local_config.url
    def setUp(self) -> None:
        login(self.driver,self.url,
              'admin','admin@123')
        # 进入到权限页面
        organization_page = OrganizationPage(self.driver)
        organization_page.click_organization_link()
        organization_page.click_authority_link()


    def tearDown(self) -> None:
        logout(self.driver)
    # 添加分组
    def test_add_group(self):
        authority_page=AuthorityPage(self.driver)
        authority_page.click_addGroup_button()
        authority_page.switch_to_frame()
        authority_page.input_groupName('新增一组')
        authority_page.input_groupDescription('新增一组')
        authority_page.click_save()

    #新增-编辑分组
    def test_edit_group(self):
        authority_page=AuthorityPage(self.driver)
        authority_page.click_addGroup_button()
        authority_page.switch_to_frame()
        authority_page.input_groupName('新增一组测试编辑')
        authority_page.get_groupName('value')
        authority_page.input_groupDescription('新增一组测试编辑')
        authority_page.click_save()
        # 编辑分组
        authority_page.refresh()
        authority_page.scrollToBottom()
        authority_page.click_editGroup()
        authority_page.switch_to_frame()
        authority_page.clear(authority_page.groupDescription_inputbox)
        authority_page.input_groupDescription('编辑一组')
        authority_page.click_save()

    # 新增-删除分组
    def test_delete_group(self):
        authority_page=AuthorityPage(self.driver)
        authority_page.click_addGroup_button()
        authority_page.switch_to_frame()
        authority_page.input_groupName('新增一组测试删除')
        authority_page.get_groupName('value')
        authority_page.input_groupDescription('新增一组测试删除')
        authority_page.click_save()
        # 删除分组
        authority_page.refresh()
        authority_page.scrollToBottom()
        authority_page.click_deleteGroup()
        authority_page.alert_accept()
    # 新增-复制分组
    def test_copy_group(self):
        # 新增分组
        authority = AuthorityPage(self.driver)
        authority.click_addGroup_button()
        authority.switch_to_frame()
        authority.input_groupName('新增一组测试复制')
        authority.get_groupName('value')
        authority.input_groupDescription('新增一组测试复制')
        authority.click_save()
        authority.refresh()
        # 复制分组
        authority.scrollToBottom()
        authority.click_copy_group()
        authority.switch_to_frame()
        authority.clear(authority.groupName_inputbox)
        authority.input_groupName('复制一组')
        authority.clear(authority.groupDescription_inputbox)
        authority.input_groupDescription('复制一组')
        authority.click_save()



if __name__=='__main__':
    unittest.main()