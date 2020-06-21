from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PAGE_BOOK_NAME = (By.XPATH, "//h1[contains(text(),'The shellcoder')]")
    PAGE_BOOK_PRICE = (By.XPATH, "//p[text()='£9.99']")
    MESSAGE_BOOK_NAME = (By.XPATH, "//div[@class='alertinner '] //strong[contains(text(),'The shellcoder')]")
    MESSAGE_BOOK_PRICE = (By.XPATH, "//div[@class='alertinner '] //strong[contains(text(),'£9.99')]")


# //h1[text()="The shellcoder's handbook"]
# //p[text()='£9.99']
