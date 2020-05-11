import unittest
from common.base_page import BasePage
from common.config_utils import local_config
from common.browser import Browser
from common.log_utils_old import logger


class SeleniumBasePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logger.info('============测试类开始执行==============')

    def setUp(self) -> None:
        logger.info('============测试方法开始执行==============')
        self.driver=Browser().get_driver()
        self.base_page=BasePage(self.driver)
        self.base_page.set_browser_max()
        self.base_page.implicitly_wait()
        self.base_page.open_url(local_config.url)


    def tearDown(self) -> None:
        logger.info('============测试方法执行完毕==============')
        self.base_page.close_tab()

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info('============测试类执行完毕==============')