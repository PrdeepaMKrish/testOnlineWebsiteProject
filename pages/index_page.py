from pages.base_page import BasePage
from pages.index_page_locators import IndexPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class IndexPage(BasePage):
    def wait_and_click_create_link(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.CREATE_LINK).click()

    def wait_and_click_whats_new(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,IndexPageLocators.whats_new).click()

    def wait_and_click_signin_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.SIGNIN_LINK).click()
    pass