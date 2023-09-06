from selenium.webdriver.common.by import By


class UserSigninPageLocators:

    USER_EMAIL_TEXT_BOX = (By.NAME, "login[username]")
    PASSWORD_TEXT_BOX = (By.NAME, "login[password]")
    SIGNIN_BUTTON = (By.ID, "send2")