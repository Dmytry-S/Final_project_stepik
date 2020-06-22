from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PAGE_BOOK_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PAGE_BOOK_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    MESSAGE_BOOK_NAME = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) > .alertinner > strong")
    MESSAGE_BOOK_PRICE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(3) > .alertinner > p > strong")

