import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen



class Test_001_Login:
    # reads data from config.ini
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    # get it from utilities.customLogger
    logger=LogGen.loggen()

    @pytest.mark.smoke
    def test_homePageTitle(self,setup):
        self.logger.info("************Test_001_Login************")
        self.logger.info("..........Verifying Home Page Title...........")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("..........Home Page Title test Passed ...........")


        else:
            # to cupture screenshot must pytest run from terminal
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("XXXXXXXXXHome Page Title test failed XXXXXXXXX")

            assert False

    def test_login(self,setup):
        self.logger.info("............Verifing Login test ............")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        acc_title = self.driver.title
        if acc_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("............Login  test Passed ............")
            self.driver.close()

        else:
            # to cupture screenshot must run from terminal
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.logger.error("XXXXXXXXXX Login  test failed XXXXXXXXXXX")
            self.driver.close()
            assert False

    ##########

