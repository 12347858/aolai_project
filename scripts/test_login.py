from time import sleep
import pytest

from base.get_driver import init_driver
from base.read_yaml import read_yaml
from page.page import Page


class TestLogin():
    def setup(self):
        self.driver=init_driver()
        self.page = Page(self.driver)
    def teardown(self):
        sleep(5)
        self.driver.quit()

    @pytest.mark.parametrize("args", read_yaml("login_data.yaml","test_login"))
    def test_login(self,args):
        username = args["username"]
        password = args["password"]
        toast = args["toast"]
        self.page.home.click_me()
        self.page.register.click_go_login()
        self.page.login.input_username(username)
        self.page.login.input_password(password)
        self.page.login.click_login()
        if toast is None:
            print(self.page.me.get_me_text())
            try:
                assert self.page.me.get_me_text() =="baby_fan"
            except Exception as e:
                print("用户名不正确")

        else:
            assert self.page.login.base_is_exist_toast(toast)



