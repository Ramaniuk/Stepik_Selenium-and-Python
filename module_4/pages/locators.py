from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") #каждый селектор — это пара: как искать и что искать.

class LoginPageLocators():
    LOGIN_FORM = (By.ID,"login_form")
    EMAIL = (By.NAME,"[name='login-username']")
    PASSWORD = (By.ID,"id_login-password")
    LOGIN_SUBMIT = (By.NAME,"login_submit")
    REGISTER_FORM = (By.ID,"register_form")
    REGISTRATION_EMAIL = (By.ID,"id_registration-email")
    REGISTRATION_PASSWORD = (By.ID, "id_registration-password1")
    REGISTRATION_SUBMIT_PASSWORD = (By.ID,"id_registration-password2")

class ItemPageLocators():
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main p")
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    MESSAGE = (By.ID, "messages")
    NEW_ITEM_NAME = (By.CSS_SELECTOR, "#messages :first-child  > .alertinner strong")
    NEW_ITEM_PRICE = (By.CSS_SELECTOR, "#messages :last-child  > .alertinner p strong")

