from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_PAGE_LINK = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_FORM = (By.ID, "login_form")
    SIGN_UP_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ITEM_ADDED_INTO_CARD_MESSAGE = (By.CSS_SELECTOR, ".alert-success:first-child .alertinner")
    ADDED_ITEM_NAME = (By.CSS_SELECTOR, ".alert-success:first-child .alertinner strong")
    INFO_ABOUT_PRICE_IN_BASKET_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner p:first-child")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner p:first-child strong")
