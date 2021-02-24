from time import sleep

from base.get_driver import init_driver


class TestLogin():
    def setup(self):
        self.driver=init_driver()
    def teardown(self):
        sleep(5)
        self.driver.quit()
    def test_login(self):
        print("hello")