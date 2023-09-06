from pages.base_page import BasePage
from pages.user_signout_page_locators import SignoutPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class SignoutPage(BasePage):
    def wait_and_click_dropdown_link(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, SignoutPageLocators.DROPDOWN_LINK).click()
