from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_book_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def should_be_correct_name_price(self):
        page_book_name = self.browser.find_element(*ProductPageLocators.PAGE_BOOK_NAME)
        page_name_text = page_book_name.text
        page_book_price = self.browser.find_element(*ProductPageLocators.PAGE_BOOK_PRICE)
        page_price_text = page_book_price.text
        message_book_name = self.browser.find_element(*ProductPageLocators.MESSAGE_BOOK_NAME)
        message_name_text = message_book_name.text
        message_book_price = self.browser.find_element(*ProductPageLocators.MESSAGE_BOOK_PRICE)
        message_price_text = message_book_price.text
        assert page_name_text == message_name_text, "Should be equal book name"
        assert page_price_text == message_price_text, "Should be equal book price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message didn't disappear"





