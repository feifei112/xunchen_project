"""
首页 页面
"""
import page
from base.base_page import BasePage


class IndesPage(BasePage):
    updte_later = page.update_later  # 击稍后更新
    mine = page.mine  #我的 按钮

    # 击稍后更新
    def click_updte_later(self):
        self.base_click_element(self.updte_later)
    # 点击 我的 按钮
    def click_mine(self):
        self.base_click_element(self.mine)