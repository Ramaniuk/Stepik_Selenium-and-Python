from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Item is presented, but should not be"

    def should_be_message_basket_is_empty(self):
        basket_empty_content = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_CONTENT)
        assert basket_empty_content.text == "Your basket is empty. Continue shopping"



