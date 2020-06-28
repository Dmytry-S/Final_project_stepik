from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_field()

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "Basket should be in url"

    def should_be_basket_field(self):
        assert self.browser.find_element(*BasketPageLocators.BASKET_PAGE), "Basket field should be on the page"

    def should_be_empty_basket(self):
        self.should_be_empty_basket_goods()
        self.should_be_empty_basket_text()

    def should_be_empty_basket_goods(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_GOODS), "Basket should be empty"

    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), "Should be text of empty basket"
