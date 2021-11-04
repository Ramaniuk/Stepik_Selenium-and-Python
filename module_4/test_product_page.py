from pages.item_page import ItemPage
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link2 = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ItemPage(browser, link)
    page.open()
    page.should_be_button_add_to_basket()
    page.click_on_basket_button()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_new_item()
    page.should_be_name_in_new_item_message()
    page.should_be_price_in_new_item_message()