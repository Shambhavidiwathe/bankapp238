
from selenium.webdriver.common.by import By

class Usermanagment_class :

    Click_on_usermanagment_buttom_Xpath = "//a[normalize-space()='User Management']"
    Text_username_ID = "username"
    Click_on_searchuser_button_Xpath = "//button[@type='submit']"
    Text_email_ID = "email"
    Click_on_savechanges_button_Xpath = "//button[@type='submit']"
    Validate_userupdate_mgs_Xpath = "//div[@class='success-message']"



    def __init__(self,driver):
        self.driver = driver
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")



    def Click_on_usermanagment_buttom(self):
        self.driver.find_element(By.XPATH, self.Click_on_usermanagment_buttom_Xpath).click()

    def Enter_username(self,username):
        self.driver.find_element(By.ID, self.Text_username_ID).send_keys(username)

    def Click_on_searchuser_button(self):
        self.driver.find_element(By.XPATH, self.Click_on_searchuser_button_Xpath).click()

    def clear_email(self):
        self.driver.find_element(By.ID, self.Text_email_ID).clear()

    def Enter_email_updated(self,email):
        self.driver.find_element(By.ID, self.Text_email_ID).send_keys(email)

    def Click_on_savechanges_button(self):
        self.driver.find_element(By.XPATH, self.Click_on_savechanges_button_Xpath).click()

    def Validate_userupdate_mgs(self):
        try:
            self.driver.find_element(By.XPATH, self.Validate_userupdate_mgs_Xpath)
            assert True
        except:
            assert False