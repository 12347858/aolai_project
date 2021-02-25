from base.base_action import BaseAction
from selenium.webdriver.common.by import By



class HomePage(BaseAction):

    def click_me(self):
        home_me = By.ID, "com.yunmall.lc:id/tab_me"
        self.base_click(home_me)
