from selenium.webdriver.common.by import By

class SignoutPageLocators:
    #CREATE_LINK = (By.CLASS_NAME, "customer-account-login page-layout-1column")
    #CREATE_LINK = (By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[3]/a') # working by direct x path
    #CREATE_LINK = (By.XPATH, "//a[text()='Create an Account']") #working by the text method
    DROPDOWN_LINK = (By.CLASS_NAME, "action switch")