from selenium.webdriver.common.by import By
class signup_class:

    Click_on_signup_button_Xpath ="/html/body/div/nav/ul/li[2]/a"
    Text_username_ID = "username"
    Text_password_ID = "password"
    Text_email_ID = "email"
    Text_phoneno_ID = "phone"
    Click_on_create_user_button_Xpath = "//button[@type='submit']"
    Succsess_mgs_class = "success-message"


    def __init__(self,driver):
        self.driver = driver
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


    def Click_on_signup_button(self):
        self.driver.find_element(By.XPATH,self.Click_on_signup_button_Xpath).click()

    def Enter_username(self,username):
        self.driver.find_element(By.ID,self.Text_username_ID).send_keys(username)

    def Enter_password(self,password):
        self.driver.find_element(By.ID,self.Text_password_ID).send_keys(password)

    def Enter_email(self,email) :
        self.driver.find_element(By.ID,self.Text_email_ID).send_keys(email)

    def Enter_phoneno(self,phoneno):
        self.driver.find_element(By.ID,self.Text_phoneno_ID).send_keys(phoneno)


    def Click_on_create_user_button(self):
        self.driver.find_element(By.XPATH,self.Click_on_create_user_button_Xpath).click()

    def Validate_user_creation(self):
        try:
            sucsess_mgs = self.driver.find_element(By.CLASS_NAME,self.Succsess_mgs_class)
            return sucsess_mgs
        except:
            pass



