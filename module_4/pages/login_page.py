from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert url.find("login") != -1

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM)

    def register_new_user(self):
        email_value = str(time.time()) + "@fakemail.org"
        password_value = "ItisMyPassword167$"
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_field.send_keys(email_value)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password_field.send_keys(password_value)
        password_confirm_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_PASSWORD)
        password_confirm_field.send_keys(password_value)
        submit_btn = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BTN)
        submit_btn.click()


