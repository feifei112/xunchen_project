from appium import webdriver

import time
def init_driver():
    capabilities = dict() # 定义一个空的字典
    capabilities["platformName"] = "Android"
    capabilities["platformVersion"] = "5.1"
    capabilities["deviceName"] = "模拟器"
    capabilities["appPackage"] = "com.bjcsxq.chat.carfriend" # 包名
    capabilities["appActivity"] = ".MainActivity" # 启动名
    # 解决输入中文
    capabilities['resetKeyboard'] = True
    capabilities['unicodeKeyboard'] = True
    # com.bjcsxq.chat.carfriend/.MainActivity
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=capabilities)
    return driver
if __name__ =="__main__":
    init_driver()


