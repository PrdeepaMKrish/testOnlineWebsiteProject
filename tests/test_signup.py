from pages.index_page import IndexPage
from pages.createaccount_page import CreateAccountPage
from resources.constants import TEST_SITE_URL
from tests.conftest import newuser_account

class TestSignup:
    def test_signup_new_user(self, driver, newuser_account):
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.wait_and_click_create_link()

        createaccount_page = CreateAccountPage(driver)
        createaccount_page.wait_and_type_first_name(newuser_account)
        createaccount_page.wait_and_type_last_name(newuser_account)
        createaccount_page.type_email(newuser_account)
        createaccount_page.type_password(newuser_account)
        createaccount_page.type_confirmpassword(newuser_account)
        createaccount_page.click_create_btn()
