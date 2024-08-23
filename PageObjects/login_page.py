import time
from selenium.webdriver.common.by import By

class login_class:

    Click_login_Xpath = "//a[normalize-space()='Login']"
    Text_username_ID = "username"
    Text_password_ID = "password"
    Click_on_login_button_Xpath = "//button[@type='submit']"
    Validate_login_page_title_Xpath = "//h2[normalize-space()='Dashboard']"
    Click_on_logout_button_Xpath = "//a[normalize-space()='Logout']"


    def __init__(self, driver):
        self.driver = driver
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


    def Click_login(self):
        self.driver.find_element(By.XPATH, self.Click_login_Xpath).click()

    def Enter_username(self, username):
        self.driver.find_element(By.ID, self.Text_username_ID).send_keys(username)

    def Enter_password(self, password):
        self.driver.find_element(By.ID, self.Text_password_ID).send_keys(password)

    def Click_on_login_button(self):
        self.driver.find_element(By.XPATH, self.Click_on_login_button_Xpath).click()

    def Validate_Login_Stauts(self):
        try:
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.Validate_login_page_title_Xpath)
            time.sleep(1)
            print("User login test case is passed")
            return "LoginPass"
        except:
            print("User login test case is failed")
            return "LoginFail"


    def Click_on_logout_button(self):
        self.driver.find_element(By.XPATH,self.Click_on_logout_button_Xpath).click()

