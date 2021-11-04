from .base_page import BasePage
from .locators import MainPageLocators
#from .login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        # Переходы между страницами. Первый способ: возвращать нужный Page Object.
        # В качестве url передаем текущий адрес.
        #return LoginPage(browser=self.browser,url=self.browser.current_url)
        #alert = self.browser.switch_to.alert
        #alert.accept()


    def should_be_login_link(self):
        assert self.browser.find_element(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        # символ *, он указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать.