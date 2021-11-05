from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_button_add_to_basket(self):
        assert self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)

    def click_on_basket_button(self):
        cart_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        cart_button.click()

    def should_be_message_about_new_item(self):
        assert self.browser.find_element(*ProductPageLocators.NEW_ITEM_NAME)

    def should_be_name_in_new_item_message(self):
        item_name_in_message = self.browser.find_element(*ProductPageLocators.NEW_ITEM_NAME)
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME)
        assert item_name_in_message.text == item_name.text

    def should_be_price_in_new_item_message(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE)
        item_message_price = self.browser.find_element(*ProductPageLocators.NEW_ITEM_PRICE)
        assert item_message_price.text == item_price.text

    def should_not_be_success_message_before_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.NEW_ITEM_NAME), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.NEW_ITEM_NAME), \
            "Success_message is presented"

    def should_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.NEW_ITEM_NAME), \
            "Success message is not disappeared"
