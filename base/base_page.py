"""
给所有的页面(PO)文件提供公共方法 基数
"""
from selenium.webdriver.support.wait import WebDriverWait
# 定义一个类
class BasePage(object):
    def __init__(self, driver: object) -> object:
        self.driver = driver

    # 封装页而面中的元素操作
    def base_short_element(self,location,timeout=5,poll = .5):
        # 显示等待
        element = WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll)\
            .until(lambda x: x.find_element(*location)) # * 表示解包的意思
        return element

    # 方法二
    # 封装点击
    # @staticmethod  #静态方法 申明
    # def base_click_element(element):
    #     element.click()

    # 输入文本信息的操作
    # @staticmethod  #静态方法 申明
    # def base_input_short(element,text):
    #     element.clear()
    #     element.send_keys(text)


    #方法二
    # 封装点击
    def base_click_element(self,location):
        element =self.base_short_element(location)
        element.click()

    # 输入文本信息的操作
    def base_input_short(self,location,text):
        element = self.base_short_element(location)
        element.clear()
        element.send_keys(text)


