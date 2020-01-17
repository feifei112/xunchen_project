"""
登录页面
"""
import page
from base.base_page import BasePage


class LoginPage(BasePage):
    # 类的属性
    login_reg = page.login_reg   # 登录按钮

    # 点击登录按钮
    def click_login_reg(self):
        self.base_click_element(self.login_reg)
