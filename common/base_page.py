import os
import time
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from common import HTMLTestReportCN
from common.config_utils import local_config
from common.log_utils import logger

class BasePage(object):
    def __init__(self,driver):
        self.driver =driver #webdriver.Chrome()

    # 浏览器操作封装 -- > 二次封装
    def open_url(self,url):
        try:
            self.driver.get( url )
            logger.info('打开url地址 %s '% url )
        except Exception as e:
            logger.error('无法打开该地址，原因是：%s'%traceback.format_exc()) #输出详细错误信息，验证没成功，依然没内容

    def set_browser_max(self):
        self.driver.maximize_window()
        logger.info('设置浏览器最大化')

    def set_browser_min(self):
        self.driver.minimize_window()
        logger.info('设置浏览器最小化')

    def refresh(self):
        self.driver.refresh()
        logger.info('浏览器刷新操作')

    def get_title(self):
        value = self.driver.title
        logger.info('获取网页标题，标题是%s'%value)
        return value

    def close_tab(self):
        self.driver.close()
        logger.info('关闭网页')

    def quit_browse(self):
        self.driver.quit()
        logger.info('退出网页')


    def wait(self,seconds=local_config.time_out):
        time.sleep(seconds)
        logger.info('固定等待【%s】秒'%seconds)

    def implicitly_wait(self,seconds=local_config.time_out):
        self.driver.implicitly_wait(seconds)
        logger.info('隐式等待【%s】秒'%seconds)

    #.....

    #元素操作封装
    # element_info = {'element_name':'用户名输入框','locator_type':'xpath','locator_value':'//input[@name="account"]','timeout': 5 }
    def find_element(self,element_info):
        '''
        根据元素参数信息查找元素
        :param element_info:元素信息 字典类型{'':'','':''}
        :return:element对象
        '''
        try:
            locator_type_name = element_info['locator_type']
            locator_value_info = element_info['locator_value']
            locator_timeout = element_info['timeout']
            if locator_type_name == 'id':
                locator_type = By.ID
            if locator_type_name == 'name':
                locator_type = By.NAME
            elif locator_type_name == 'class':
                locator_type = By.CLASS_NAME
            elif locator_type_name == 'xpath':
                locator_type = By.XPATH
            element = WebDriverWait(self.driver,locator_timeout)\
                .until(lambda x:x.find_element(locator_type,locator_value_info))
            logger.info('[%s]元素识别成功'%element_info['element_name'])
            # element = WebDriverWait(self.driver, locator_timeout)\
            #     .until(EC.presence_of_element_located((locator_type, locator_value_info)))
        except Exception as e:
            logger.error('[%s]元素不能识别，原因是%s' % (element_info['element_name'],e.__str__()))
            self.screenshot_asfile()
        return element

    def click(self,element_info):
        try:
            element = self.find_element(element_info)
            element.click()
            logger.info('[%s]元素进行点击操作'%element_info['element_name'])
        except Exception as e :
            logger.error('[%s]元素进行点击失败，原因是：%s'%(element_info['element_name'],e.__str__()))
            self.screenshot_asfile()
    def get_value(self,element_info,attribute):
        try:
            element = self.find_element(element_info)
            return element.get_attribute(attribute)
            logger.info('获取[%s]的属性值'%element_info['element_name'])
        except Exception as e:
            logger.error('[%s]元素获取失败，原因是：%s' % (element_info['element_name'], e.__str__()))

    def input(self,element_info,content):
        try:
            element = self.find_element(element_info)
            element.send_keys(content)
            logger.info('[%s]元素输入内容：%s' %(element_info['element_name'],content))
        except Exception as e:
            logger.error('[%s]元素输入失败，原因是：%s' % (element_info['element_name'], e.__str__()))
        
    def get_text(self,element_info):
        element = self.find_element(element_info)
        return  element.text

    def switchToFrame(self,element_info):
        try:
            element = self.find_element(element_info)
            self.driver.switch_to.frame(element)
            logger.info('[%s]iframe跳转'%element_info['element_name'])
        except Exception as e:
            logger.error('框架跳转失败，原因是：%s' % e.__str__())

    def scrollIntoView(self,element_info):
        try:
            element = self.find_element(element_info)
            self.driver.execute_script('arguments[0].scrollIntoView();', element)
            self.wait(2)
            logger.info('浏览器滚动到元素【%s】的位置'%element_info['element_name'])
        except Exception as e:
            logger.error('下拉到[%S]元素失败，原因是：%s' %(element_info['element_name'],e.__str__()))

    def scrollToBottom(self):
        try:
            self.driver.execute_script('document.documentElement.scrollTop=100000;')# 浏览器滚动条下滑操作到底部
            self.wait()
            logger.info('浏览器下滑到底部操作')
        except Exception as e:
            logger.error('浏览器滚动到底部失败，原因是：%s' % e.__str__())

    def clear(self,element_info):
        try:
            element = self.find_element(element_info)
            element.clear()
            logger.info('[%s]元素进行输入框清除操作'%element_info['element_name'])
        except Exception as e:
            logger.error('清除[%s]元素失败，原因是：%s'%(element_info['element_name'],e.__str__()))

    def select(self,element_info,content):
        element = self.find_element(element_info)
        Select(element).select_by_visible_text(content)
        logger.info('[%s]元素进行下拉选择操作'%element_info['element_name'])

    def switch_to_alert(self,actions='accept',time_out=local_config.time_out):
        WebDriverWait(self.driver,time_out).until(EC.alert_is_present())
        alert=self.driver.switch_to.alert
        alert_text=alert.text
        if actions=='accept':
            alert.accept()
        elif actions=='dismiss':
            alert.dismiss()
        return alert_text
        logger.info('弹框内容是：%s'%alert_text)


    #selenium执行js代码
    def execute_script(self,js_str,element_info=None):
        if element_info:
            self.driver.execute_script(js_str)
        else:
            self.driver.execute_script(js_str,None)

    #移除属性
    def delete_element_attribute(self,element_info,attribute_name):
        element = self.find_element(element_info)
        self.execute_script('arguments[0].removeAttribute("%s");'%attribute_name,element)
        logger.info('[%s]元素进行属性移除操作'%element_info['element_name'])

    # 重新设置属性
    def set_element_attribute(self,element_info,attribute_name,attribute_value):
        element = self.find_element(element_info)
        self.execute_script('arguments[0].setAttribute("%s","%s");'%(attribute_name,attribute_value),element)
        logger.info('[%s]元素进行属性设置操作' % element_info['element_name'])

    # 鼠标键盘封装
    def move_to_elements(self,element_info):
        '''
        鼠标键盘操作：移动到元素上
        :param element_info: 元素信息
        :return:
        '''
        element = self.find_element(element_info)
        ActionChains(self.driver).move_to_element(element).perform()

    def long_press_element(self,element_info,senconds):
        '''
        鼠标键盘操作：长按某个元素
        :param element_info: 元素信息
        :param senconds:
        :return:
        '''
        element = self.find_element(element_info)
        ActionChains(self.driver).click_and_hold(element).pause(senconds).release(element)

    def ctrl_v(self,element_info):
        element = self.find_element(element_info)
        element.send_keys(Keys.CONTROL,'v')
        logger.info('在元素[%s]上进行ctrl+v粘贴操作'%element_info['element_name'])

    def get_current_handle(self):
        return self.driver.current_window_handle
        logger.info('获取当前窗口的句柄')

    def switch_to_window(self,handle):
        self.driver.switch_to.window(handle)
        logger.info('根据句柄[%s]切换window'%handle)


    def switch_to_window_by_titleName(self,titleName):
        '''
        根据页面是否包含titleName切换句柄
        :param titleName: 页面的title名称
        :return:
        '''
        for handle in self.driver.window_handles:
            if WebDriverWait(self.driver,local_config.time_out).until(EC.title_contains(titleName)):
                self.driver.switch_to.window(handle)
                break
        logger.info('根据当前页面title包含[%s]切换句柄'%titleName)

    def switch_to_window_by_url(self,url):
        '''
        根据页面是否包含URL切换句柄
        :param url: 页面包含的URL地址
        :return:
        '''
        for handle in self.driver.window_handles:
            if WebDriverWait(self.driver,local_config.time_out).until(EC.url_contains(url)):
                self.driver.switch_to.window(handle)
                break
        logger.info('根据当前页面url包含[%s]切换句柄'%url)

    def screenshot_asfile(self):
        report_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', local_config.report_path)
        report_dir = HTMLTestReportCN.ReportDirectory(report_path)
        report_dir.get_screenshot(self.driver)

    def screenshot_asfile_old(self,*screen_path):
        '''
        截图并存放在文件夹中
        :param screen_path: 截图存放路径
        :return:
        '''
        current_path=os.path.dirname(__file__)
        if len(screen_path)==0:
            screenshot_filepath=local_config.screenshot_path
        else:
            screenshot_filepath=screen_path[0]
        now=time.strftime('%Y-%m-%d-%H-%M-%S')
        screenshot_filepath=os.path.join(current_path,'..',screenshot_filepath,'screentshot_%s.png'%now)
        self.driver.get_screenshot_as_file(screenshot_filepath)




















