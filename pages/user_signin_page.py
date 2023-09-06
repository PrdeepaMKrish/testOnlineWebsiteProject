from pages.base_page import BasePage
from pages.user_signin_page_locators import UserSigninPageLocators
from resources.constants import MAX_WAIT_INTERVAL
class SigninPage(BasePage):

    def wait_and_type_user_name(self, userNameAndPwList):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, UserSigninPageLocators.USER_EMAIL_TEXT_BOX).send_keys(
            userNameAndPwList[0],"@gmail.com")

    def type_password(self, userNameAndPwList):
        self.find_element(UserSigninPageLocators.PASSWORD_TEXT_BOX).send_keys(
            userNameAndPwList[1])

    def click_signin_btn(self):
        self.find_element(UserSigninPageLocators.SIGNIN_BUTTON).click()