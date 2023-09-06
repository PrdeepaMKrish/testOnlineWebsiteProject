from selenium.webdriver.common.by import By


class UserCreateAccountPageLocators:

    NEW_USER_FIRSTNAME = (By.ID, "firstname")
    NEW_USER_LASTNAME = (By.ID, "lastname")
    NEW_USER_EMAIL = (By.ID, "email_address")
    NEW_USER_PASSWORD = (By.ID, "password")
    NEW_USER_CONFIRM_PASSWORD = (By.ID, "password-confirmation")
    #CREATE_BUTTON = (By.XPATH, "/html/body/div[2]/main/div[3]/div/form/div/div[1]/button") #direct method
    #CREATE_BUTTON = (By.XPATH,"//button[@title='Create an Account']") #Button method
    CREATE_BUTTON = (By.XPATH, "//button[@title='Create an Account' and contains(@class, 'primary')]")#button method with specific class 1