import time


from selenium import webdriver
from PageObjects.user_managment_page import Usermanagment_class
from PageObjects.login_page import login_class
from Utilities.read_configfile import ReadConfigfile
from Utilities.logger import Log_class


class Test_usermanagment:
    username = ReadConfigfile.GetUsername()
    password = ReadConfigfile.GetPassword()
    log = Log_class.log_generator()

    def test_user_managment_004(self, setup):
        self.log.info("Testcase test_user_managment_004 is started ")
        self.driver = setup
        self.log.info("Opening browser")
        self.lp = login_class(self.driver)
        self.lp.Click_login()
        self.log.info("Entering username")
        self.lp.Enter_username(self.username)
        self.log.info("Entering password")
        self.lp.Enter_password(self.password)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.lp.Click_on_login_button()
        self.um = Usermanagment_class(self.driver)
        self.um.Click_on_usermanagment_buttom()
        self.log.info("Entering username for usermanagment")
        self.um.Enter_username(self.username)
        self.um.Click_on_searchuser_button()
        self.log.info("Deleting present email ")
        self.um.clear_email()
        self.log.info("Updating email")
        self.um.Enter_email_updated("saanvi@123")
        self.um.Click_on_savechanges_button()
        time.sleep(2)
        self.log.info("Validating user updation")
        if self.um.Validate_userupdate_mgs == "User updated successfully":
            try:
                self.log.info("Testcase test_user_managment_004 is pass ")
                self.log.info("Taking screenshot")
                self.driver.save_screenshot(".\\Screenshots\\test_user_managment_004_pass.png")
                assert True
            except:
                self.log.info("Testcase test_user_managment_004 is fail ")
                self.log.info("Taking screenshot")
                self.driver.save_screenshot(".\\Screenshots\\test_user_managment_004_fail.png")
                self.log.info("Testcase test_user_managment_004 is completed ")
                assert False
        self.log.info("Testcase test_user_managment_004 is completed ")
