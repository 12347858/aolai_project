from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
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
        return self.base_find(loc).text
    #toast:为部分文本
    #根据部分文本判断toast书否存在，存在返回TRUE，不存在返回False
    def base_is_exist_toast(self,toast):
        toast_message = By.XPATH,"//*[contains(@text,'%s')]" %toast
        try:
            self.base_find(toast_message)
            return True
        except TimeoutException:
            return False

    def base_get_toast_text(self,toast):
        if self.base_is_exist_toast(toast) is True:
            toast_message = By.XPATH, "//*[contains(@text,'%s')]" % toast
            return self.base_find(toast_message).text
        else:
            raise Exception("toast为出现，请检查参数是否正确。")
