from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url == LoginPageLocators.LOGIN_PAGE_LINK, "Incorrect login page url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.SIGN_UP_FORM), "Sign up form is not presented"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_ADDRESS_INPUT)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_INPUT)
        password_input.send_keys(password)
        password_conform_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD_INPUT)
        password_conform_input.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGUSTRATION_REGISTER_BUTTON)
        register_button.click()