from .base_page import BasePage
from .locators import ItemPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ItemPage(BasePage):
    def should_be_button_add_to_basket(self):
        assert self.browser.find_element(*ItemPageLocators.BASKET_BUTTON)

    def click_on_basket_button(self):
        cart_button = self.browser.find_element(*ItemPageLocators.BASKET_BUTTON)
        cart_button.click()

    def should_be_message_about_new_item(self):
        assert self.browser.find_element(*ItemPageLocators.MESSAGE)

    def should_be_name_in_new_item_message(self):
        item_name_in_message = self.browser.find_element(*ItemPageLocators.NEW_ITEM_NAME)
        item_name = self.browser.find_element(*ItemPageLocators.ITEM_NAME)
        print(item_name.text)
        print(item_name_in_message.text)
        assert (item_name_in_message.text) == item_name.text

    def should_be_price_in_new_item_message(self):
        item_price = self.browser.find_element(*ItemPageLocators.ITEM_PRICE)
        item_message_price = self.browser.find_element(*ItemPageLocators.NEW_ITEM_PRICE)
        assert item_message_price.text == item_price.text






