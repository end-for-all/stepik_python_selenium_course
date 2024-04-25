from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_guest_basket_page(self):
        self.should_be_basket_page_url()
        self.should_be_no_items_in_basket_for_guest()
        self.should_be_message_about_no_item_in_basket()

    def should_be_basket_page_url(self):
        assert self.browser.current_url == BasketPageLocators.BASKET_PAGE_URL, "Incorrect basket page url"

    def should_be_no_items_in_basket_for_guest(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket for guest is not empty"

    def should_be_message_about_no_item_in_basket(self):
        assert self.is_element_present(
            *BasketPageLocators.MESSAGE_ABOUT_EMPTY_BASKET), "There is no message about empty basket"
        expected_message_text = "Your basket is empty. Continue shopping"
        actual_message_text = self.browser.find_element(*BasketPageLocators.MESSAGE_ABOUT_EMPTY_BASKET).text
        assert actual_message_text == expected_message_text, f"Message text is {actual_message_text}, instead of {expected_message_text}"
