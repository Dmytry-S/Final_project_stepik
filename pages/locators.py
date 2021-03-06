from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a.btn.btn-default")
    BASKET_PAGE = (By.CSS_SELECTOR, ".page-header.action")
    BASKET_GOODS = (By.CSS_SELECTOR, ".basket_items")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner > p")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_FIELD = (By.XPATH, "//input[@name='registration-email']")
    PASSWORD_1 = (By.XPATH, "//input[@name='registration-password1']")
    PASSWORD_2 = (By.XPATH, "//input[@name='registration-password2']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@name='registration_submit']")
    password = "123ton789"


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PAGE_BOOK_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PAGE_BOOK_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    MESSAGE_BOOK_NAME = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) > .alertinner > strong")
    MESSAGE_BOOK_PRICE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(3) > .alertinner > p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.fade:nth-child(1)")
