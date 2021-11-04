from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") #каждый селектор — это пара: как искать и что искать.

class LoginPageLocators():
    LOGIN_FORM = (By.ID,"#ilogin_form")
    EMAIL = (By.NAME,"[name='login-username']")
    PASSWORD = (By.ID,"#id_login-password")
    LOGIN_SUBMIT = (By.NAME,"[name = 'login_submit']")
    REGISTER_FORM = (By.ID,"#register_form")
    REGISTRATION_EMAIL = (By.ID,"#id_registration-email")
    REGISTRATION_PASSWORD = (By.ID, "#id_registration-password1")
    REGISTRATION_SUBMIT_PASSWORD = (By.ID,"#id_registration-password2")



