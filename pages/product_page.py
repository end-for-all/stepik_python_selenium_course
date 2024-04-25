from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_item_to_the_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()

    def should_be_message_about_item_was_added_to_card(self):
        assert self.is_element_present(
            *ProductPageLocators.ITEM_ADDED_INTO_CARD_MESSAGE), "There is no message about item was added into card"
        expected_item_name = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        actual_item_name = self.browser.find_element(*ProductPageLocators.ADDED_ITEM_NAME).text
        assert expected_item_name == actual_item_name, f"Item name in message equal {actual_item_name} instead of {expected_item_name}"

    def should_be_message_about_total_price_in_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.INFO_ABOUT_PRICE_IN_BASKET_MESSAGE), "There is no message about total price in basket"
        expected_item_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        actual_item_price = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        assert actual_item_price == expected_item_price, f"Item price in message equal {actual_item_price} instead of {expected_item_price}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.ITEM_ADDED_INTO_CARD_MESSAGE), "Success message is presented, but should not be"

    def should_not_be_visible_success_message_after_some_time(self):
        assert self.is_disappeared(
            *ProductPageLocators.ITEM_ADDED_INTO_CARD_MESSAGE), "Success message is still visible, but should not be"
