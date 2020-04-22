from selenium.webdriver.common.by import By
from element_infos.login_page import LoginPage


def login(driver,url,username,password):
    login_page = LoginPage(driver)
    login_page.open_url(url)
    login_page.set_browser_max()
    login_page.input_username(username)
    login_page.input_password(password)
    login_page.click_login()