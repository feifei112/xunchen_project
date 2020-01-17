"""
我的页面
"""
import page
from base.base_page import BasePage


class MinePage(BasePage):
    phone_log= page.phone_log  # 手机号码
    pwd_log = page.pwd_log   # 密码
    log = page.log  # 登录
    confirm_btn = page.confirm_btn  # 确认

    # 输入 手机号码
    def input_phone_log(self,phone):
        self.base_input_short(self.phone_log,phone)
    # 输入密码
    def input_pwd_log(self,pwd):
        self.base_input_short(self.pwd_log,pwd)
    # 点击登录
    def click_log(self):
        self.base_click_element(self.log)
    # 点击确认
    def click_confirm_btn(self):
        self.base_click_element(self.confirm_btn)