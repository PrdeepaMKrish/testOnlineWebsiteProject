from test_utils import *
from pages.index_page import IndexPage

from pages.user_signin_page import SigninPage

from pages.user_signout_page import SignoutPage

from pages.user_signin_success_page import UserSuccessPage

from resources.constants import TEST_SITE_URL
from tests.conftest import search_item


class TestSignin:

    # Test Case 1 ( Registering the user)
    def test_signin_new_user(self, driver, username_password):
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.wait_and_click_signin_button()


        user_signin_page = SigninPage(driver)
        user_signin_page.wait_and_type_user_name(username_password)
        user_signin_page.type_password(username_password)
        user_signin_page.click_signin_btn()

        #user_signout_page = SignoutPage(driver)
        #user_signout_page.wait_and_click_dropdown_link()

        #subscribe_page = SubscribePage(driver)
        #subscribe_page.click_subscribe_link()

        #search_page = SearchPage(driver)
        #search_page.wait_and_type_item_name(search_item)
        #search_page.press_enter()


        #user_signin_success_page = UserSuccessPage(driver)
        #user_success_lbl = user_signin_success_page.get_signin_success_label()
        #assert user_success_lbl.__contains__("Welcome,(username_password[0])!")

