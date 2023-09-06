from pages.base_page import BasePage
from pages.createaccount_page_locators import UserCreateAccountPageLocators
from resources.constants import MAX_WAIT_INTERVAL
class CreateAccountPage(BasePage):
    def wait_and_type_first_name(self, userDetailsAndPwList):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, UserCreateAccountPageLocators.NEW_USER_FIRSTNAME).send_keys(
            userDetailsAndPwList[0])

    def wait_and_type_last_name(self, userDetailsAndPwList):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, UserCreateAccountPageLocators.NEW_USER_LASTNAME).send_keys(
            userDetailsAndPwList[1])

    def type_email(self, userDetailsAndPwList):
        self.find_element(UserCreateAccountPageLocators.NEW_USER_EMAIL).send_keys(
            userDetailsAndPwList[2])

    def type_password(self, userDetailsAndPwList):
        self.find_element(UserCreateAccountPageLocators.NEW_USER_PASSWORD).send_keys(
            userDetailsAndPwList[3])

    def type_confirmpassword(self, userDetailsAndPwList):
        self.find_element(UserCreateAccountPageLocators.NEW_USER_CONFIRM_PASSWORD).send_keys(
            userDetailsAndPwList[4])

    def click_create_btn(self):
        self.find_element(UserCreateAccountPageLocators.CREATE_BUTTON).click()