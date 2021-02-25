from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class RegisterPage(BaseAction):
    #点击已有账号，去登录
    def click_go_login(self):
        register_login = By.ID, "com.yunmall.lc:id/textView1"
        self.base_click(register_login)