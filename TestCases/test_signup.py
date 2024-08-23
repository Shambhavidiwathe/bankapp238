import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.signup_page import signup_class
from Utilities.logger import Log_class


class Test_singup_class:
    log = Log_class.log_generator()


    def test_signup_url_001(self,setup):
        self.log.info("Testcase test_signup_url_001 is started")
        self.driver = setup
        self.log.info("Opening browser")
        self.driver.maximize_window()
        self.log.info("Cheking page title")
        if self.driver.title == "Bank Application":
            self.log.info("Testcase test_signup_url_001 is pass")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_signup_url_001_pass.png")
            assert True
        else:
            self.log.info("Testcase test_signup_url_001 is fail")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_signup_url_001_fail.png")
            self.log.info("Testcase test_signup_url_001 is completed \n")
            assert False
        self.log.info("Testcase test_signup_url_001 is completed \n")




    def test_signup_createuser_002(self,setup):
        self.log.info("Testcase test_signup_createuser_002 is started")
        self.driver = setup
        self.log.info("Opening browser")
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.su = signup_class(self.driver)
        self.su.Click_on_signup_button()
        self.log.info("Entering username")
        self.su.Enter_username("Sanvi")
        self.log.info("Entering password")
        self.su.Enter_password("S@nvi123")
        self.log.info("Entering email")
        self.su.Enter_email("sanvi@123.com")
        self.log.info("Entering phone no")
        self.su.Enter_phoneno("9456765898")
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.su.Click_on_create_user_button()
        time.sleep(3)
        self.log.info("Validating user creation")
        if self.su.Validate_user_creation == "User created successfully":
            try:
                self.log.info("Testcase test_signup_createuser_002 is pass")
                self.log.info("Taking screenshot")
                self.driver.save_screenshot(".\\Screenshots\\test_signup_createuser_002_pass.png")
                assert True
            except:
                self.log.info("Testcase test_signup_createuser_002 is fail ")
                self.log.info("Taking screenshot")
                self.driver.save_screenshot(".\\Screenshots\\test_signup_createuser_002_fail.png")
                self.log.info("Testcase test_signup_createuser_002 is completed \n")
                assert False
        self.log.info("Testcase test_signup_createuser_002 is completed \n")
