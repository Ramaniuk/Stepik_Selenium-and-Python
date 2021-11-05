from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  # каждый селектор — это пара: как искать и что искать.
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR,".btn-group a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_FORM = (By.ID,"login_form")
    EMAIL = (By.NAME,"[name='login-username']")
    PASSWORD = (By.ID,"id_login-password")
    LOGIN_SUBMIT = (By.NAME,"login_submit")
    REGISTER_FORM = (By.ID,"register_form")
    REGISTRATION_EMAIL = (By.ID,"id_registration-email")
    REGISTRATION_PASSWORD = (By.ID, "id_registration-password1")
    REGISTRATION_SUBMIT_PASSWORD = (By.ID,"id_registration-password2")
    REGISTRATION_SUBMIT_BTN = (By.NAME, "registration_submit")


class ProductPageLocators():
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main p")
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    NEW_ITEM_NAME = (By.CSS_SELECTOR, "#messages :first-child  > .alertinner strong")
    NEW_ITEM_PRICE = (By.CSS_SELECTOR, "#messages :last-child  > .alertinner p strong")


class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, "basket-items")
    BASKET_EMPTY_CONTENT = (By.CSS_SELECTOR, "#content_inner p")
