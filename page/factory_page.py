"""
入口页面   工厂页面
"""
from page.index_page import IndesPage
from page.login_page import LoginPage
from page.mine_page import MinePage


class FactoryPage(object):
    def __init__(self,driver):
        self.driver = driver

    # 首页 页面
    def index_page(self):
        return IndesPage(self.driver)

    # 我的页面
    def mine_page(self):
        return MinePage(self.driver)

    # 登录页面
    def login_page(self):
        return LoginPage(self.driver)