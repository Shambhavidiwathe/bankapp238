import time
import pytest

from PageObjects.login_page import login_class
from Utilities import Excel_utils
from Utilities.logger import Log_class



class Test_login_DDT:
    log = Log_class.log_generator()
    file_path = ".\\TestCases\\test_data\\test_data.xlsx"

    def test_login_ddt_006(self, setup):
        self.log.info("test_login_ddt_006_pass is Started \n")
        self.driver = setup
        self.log.info("Opening browser")
        self.lp = login_class(self.driver)
        self.lp.Click_login()
        self.log.info("Counting no of rows")
        self.rows = Excel_utils.get_rowCount(self.file_path, "login_data")
        print("no of rows in excel test data ---> " + str(self.rows))
        self.log.info("Reading data from excelsheet ")
        List_status = []
        for r in range(2, self.rows + 1):
            self.username = Excel_utils.readData(self.file_path, "login_data", r, 2)
            self.password = Excel_utils.readData(self.file_path, "login_data", r, 3)
            self.Excel_Result = Excel_utils.readData(self.file_path, "login_data", r, 4)
            self.log.info("Entering Username-->" + self.username)
            self.lp.Enter_username(self.username)
            self.log.info("Entering Password-->" + self.password)
            self.lp.Enter_password(self.password)
            self.log.info("Clicking on login button")
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            self.lp.Click_on_login_button()
            self.log.info("Verifying the login status")


            if self.lp.Validate_Login_Stauts() == "LoginPass" and self.Excel_Result == "LoginPass":
                List_status.append("Pass")
                self.log.info("writing data to excelsheet")
                Excel_utils.writeData(self.file_path, "login_data", r, 5, "Pass")
                self.log.info("Taking the screenshot")
                self.driver.save_screenshot(".\\Screenshots\\test_login_ddt_006_pass.png")
                self.log.info("Clicking on logout button")
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                self.lp.Click_on_logout_button()

            elif self.lp.Validate_Login_Stauts() == "LoginPass" and self.Excel_Result == "LoginFail":
                List_status.append("Fail")
                self.log.info("writing data to excelsheet")
                Excel_utils.writeData(self.file_path, "login_data", r, 5, "Fail")
                self.log.info("Taking a screenshot")
                self.driver.save_screenshot(".\\Screenshots\\test_login_ddt_006_fail.png")
                # self.lp.Click_on_logout_button()
            elif self.lp.Validate_Login_Stauts() == "LoginFail" and self.Excel_Result == "LoginPass":
                List_status.append("Fail")
                self.log.info("writing data to excelsheet")
                Excel_utils.writeData(self.file_path, "login_data", r, 5, "Fail")
                self.log.info("Taking a screenshot")
                self.driver.save_screenshot(".\\Screenshots\\test_login_ddt_006_fail.png")
                # self.lp.Click_on_logout_button()
            elif self.lp.Validate_Login_Stauts() == "LoginFail" and self.Excel_Result == "LoginFail":
                List_status.append("Pass")
                self.log.info("writing data to excelsheet")
                Excel_utils.writeData(self.file_path, "login_data", r, 5, "Pass")
                self.log.info("Taking a screenshot")
                self.driver.save_screenshot(".\\Screenshots\\test_login_ddt_006_pass.png")
                # self.lp.Click_on_logout_button()

        print(List_status)
        if "Fail" not in List_status:
            self.log.info("test_login_ddt_006_pass is passed")
            assert True
        else:
            self.log.info("test_login_ddt_006_pass is failed")
            assert False

        self.driver.quit()
        self.log.info("Closing the browser")
        self.log.info("test_login_ddt_006_pass is completed")
