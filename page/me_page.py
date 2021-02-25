from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MePage(BaseAction):
    def get_me_text(self):
        me_username = By.ID,"com.yunmall.lc:id/tv_user_nikename"
        return self.base_get_text(me_username)
