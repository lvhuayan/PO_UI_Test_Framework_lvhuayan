import unittest
from common.base_page import BasePage
from common.config_utils import local_config
from common.browser import Browser


class SeleniumBasePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    def setUp(self) -> None:
        self.driver=Browser().get_driver()
        self.base_page=BasePage(self.driver)
        self.base_page.set_browser_max()
        self.base_page.implicitly_wait()
        self.base_page.open_url(local_config.url)


    def tearDown(self) -> None:
        self.base_page.close_tab()

    @classmethod
    def tearDownClass(cls) -> None:
        pass