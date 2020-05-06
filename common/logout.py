from element_infos.logout.logout_page import LogoutPage

def logout(driver):
    logout_page = LogoutPage(driver)
    logout_page.click_username()
    logout_page.click_logout()
