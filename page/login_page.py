from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    def input_username(self,values):
        login_username = By.ID,"com.yunmall.lc:id/logon_account_textview"
        self.base_input(login_username,values)

    def input_password(self,values):
        login_password = By.ID, "com.yunmall.lc:id/logon_password_textview"
        self.base_input(login_password,values)

    def click_login(self):
        login_click_login = By.XPATH,"//*[@text='登录']"
        self.base_click(login_click_login)
