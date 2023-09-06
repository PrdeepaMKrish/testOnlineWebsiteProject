import pytest as pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def username_password():
    user_name = "demouser"
    password = "demouser@123"
    return [user_name, password]

@pytest.fixture(scope="function")
def newuser_account():
    first_name = "demo"
    last_name = "user"
    user_email = "demouser@gmail.com"
    password = "demouser@123"
    confirm_password = "demouser@123"
    return [first_name, last_name, user_email, password, confirm_password]

@pytest.fixture(scope="function")
def search_item():
    item_name = "bag"
    return [item_name]

@pytest.fixture(scope="module")
def driver():
    _driver = webdriver.Chrome()
    yield _driver
    _driver.quit()
