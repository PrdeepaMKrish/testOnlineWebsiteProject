from pages.base_page import BasePage
from pages.user_sigin_success_locators_page import UserSuccessPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class UserSuccessPage(BasePage):

    def get_signin_success_label(self):
        lbl_signin_success_txt = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, UserSuccessPageLocators.SIGNIN_SUCCESS_LBL).text
        return lbl_signin_success_txt