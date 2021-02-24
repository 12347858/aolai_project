from selenium.webdriver.support.wait import WebDriverWait
class BaseAction():
    def __init__(self,driver):
        self.driver=driver
    def base_find(self,loc,timeout=30,poll=0.5):
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(lambda x: x.find_element(*loc))
    def base_click(self,loc):
        self.base_find(loc).click()
    def base_input(self,loc,values):
        self.base_find(loc).send_keys(values)
    def base_clear(self,loc):
        self.base_find(loc).clear()
    def base_get_text(self,loc):
        pass

