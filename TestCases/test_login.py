import time

from PageObjects.login_page import login_class
from Utilities.read_configfile import ReadConfigfile
from Utilities.logger import Log_class

class Test_login_class:
    username = ReadConfigfile.GetUsername()
    password = ReadConfigfile.GetPassword()
    log = Log_class.log_generator()

    def test_login_003(self, setup):
        self.log.info("Testcase test_login_003 is started")
        self.driver = setup
        self.log.info("Opening Browser")
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.lp = login_class(self.driver)
        self.lp.Click_login()
        self.log.info("Entering username")
        self.lp.Enter_username(self.username)
        self.log.info("Entering password")
        self.lp.Enter_password(self.password)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)
        self.lp.Click_on_login_button()
        self.log.info("Cheking on title")
        if self.driver.title == "Dashboard":
            self.log.info("Testcase test_login_003 is pass")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_login_003_pass.png")
            assert True
        else:
            self.log.info("Testcase test_login_003 is fail")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_login_003_fail.png")
            self.log.info("Testcase test_login_003 is completed \n")
            assert False
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.lp.Click_on_logout_button()
        self.log.info("Testcase test_login_003 is completed \n")



