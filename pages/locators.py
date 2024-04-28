from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_PAGE_LINK = (By.CSS_SELECTOR, "[href='/en-gb/basket/']:first-child")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_PAGE_LINK = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_FORM = (By.ID, "login_form")
    SIGN_UP_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL_ADDRESS_INPUT = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD_INPUT = (By.ID, "id_registration-password1")
    REGISTRATION_CONFIRM_PASSWORD_INPUT = (By.ID, "id_registration-password2")
    REGUSTRATION_REGISTER_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ITEM_ADDED_INTO_CARD_MESSAGE = (By.CSS_SELECTOR, ".alert-success:first-child .alertinner")
    ADDED_ITEM_NAME = (By.CSS_SELECTOR, ".alert-success:first-child .alertinner strong")
    INFO_ABOUT_PRICE_IN_BASKET_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner p:first-child")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner p:first-child strong")

class BasketPageLocators():
    BASKET_PAGE_URL = "https://selenium1py.pythonanywhere.com/en-gb/basket/"
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
    MESSAGE_ABOUT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")
