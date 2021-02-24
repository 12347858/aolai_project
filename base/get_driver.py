from appium import webdriver
def init_driver():
    #创建一个字典
    desired_caps = dict()
    #手机平台(Android,ios)
    desired_caps['platformName'] = 'Android'
    #手机的版本号
    desired_caps['platformVersion'] = '5.1'
    #手机的版本号(可随便写，不能不写)
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # 输入中文设置
    desired_caps['unicodekeyboard'] = True
    desired_caps['resetkeyboard'] = True

    # 启动程序的包名
    desired_caps['appPackage'] = 'com.yunmall.lc'
    # 启动程序的界面名
    desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'
    # 链接Appium服务器
    return  webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)