import time

from Utilities.read_configfile import ReadConfigfile
from PageObjects.login_page import login_class
from Utilities.logger import Log_class

class Test_login_params:
    username = ReadConfigfile.GetUsername()
    password = ReadConfigfile.GetPassword()
    log = Log_class.log_generator()


    def test_login_paramitor_005(self,setup,getdataforlogin):
        self.log.info("Testcase test_login_005 is started \n")
        self.driver = setup
        self.log.info("Opening Browser")
        self.lp = login_class(self.driver)
        self.lp.Click_login()
        self.log.info("Entering username")
        self.lp.Enter_username(getdataforlogin[0])
        self.log.info("Entering password")
        self.lp.Enter_password(getdataforlogin[1])
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.lp.Click_on_login_button()

        self.log.info("validating logins with diffrent data")

        if self.lp.Validate_Login_Stauts() == "LoginPass" and getdataforlogin[2] == "LoginPass":
            self.log.info("taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_login_paramitor_005_pass.png")
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            self.lp.Click_on_logout_button()
            assert True
        elif self.lp.Validate_Login_Stauts() == "LoginPass" and getdataforlogin[2] == "LoginFail":
             self.log.info("taking screenshot")
             self.driver.save_screenshot(".\\Screenshots\\test_login_paramitor_005_fail.png")
             assert False
        elif self.lp.Validate_Login_Stauts() == "LoginFail" and getdataforlogin[2] == "LoginPass":
             self.log.info("taking screenshot")
             self.driver.save_screenshot(".\\Screenshots\\test_login_paramitor_005_fail.png")
             assert False
        elif self.lp.Validate_Login_Stauts() == "LoginFail" and getdataforlogin[2] == "LoginFail":
             self.log.info("taking screenshot")
             self.driver.save_screenshot(".\\Screenshots\\test_login_paramitor_005_pass.png")
             assert True
        self.log.info("Testcase test_login_005 is completed \n")
