import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from common.config_utils import local_config

current_path=os.path.dirname(__file__)
dri_path=os.path.join(current_path,'..',local_config.driver_path)

class Browser():
    def __init__(self,driver_path=dri_path,driver_name=local_config.driver_name):
        self.driver_path=driver_path
        self.driver_name = driver_name

    def get_driver(self):
        if self.driver_name.lower()=='chrome':
            return self.get_chrome_driver()
        elif self.driver_name.lower()=='firefox':
            return self.get_firefox_driver()
        elif self.driver_name.lower()=='edge':
            return self.get_edge_driver()

    def get_chrome_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('lang=zh_CN.UTF-8')  #设置默认编码为utf-8
        chrome_options.add_experimental_option('useAutomationExtension', False)#取消chrome受自动控制提示
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])#取消chrome受自动控制提示
        chrome_driver_path=os.path.join(self.driver_path,'chromedriver.exe')
        driver=webdriver.Chrome(options=chrome_options,executable_path=chrome_driver_path,)
        return driver

    def get_firefox_driver(self):
        firefox_driver_path=os.path.join(self.driver_path,'geckodriver.exe')
        driver=webdriver.Firefox(executable_path=firefox_driver_path)
        return driver

    def get_edge_driver(self):
        edge_driver_path=os.path.join(self.driver_path,'MicrosoftWebDriver.exe')
        driver=webdriver.Edge(executable_path=edge_driver_path)
        return driver
    def __get_remote_driver(self):  # selenium支持分布式 grid == > 配置（你自己的代码编写、配置）
        pass

if __name__=='__main__':
    browser=Browser()
    browser.get_chrome_driver()
