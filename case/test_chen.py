from page.factory_page import FactoryPage
from utils import init_driver
import pytest
import time
class TestChen(object):
   """测试学车不软件登录页面"""
   @pytest.fixture(autouse=True)
   def test_func(self):
        self.driver = init_driver() # 驱动化设备实例对象
        self.factor_page = FactoryPage(self.driver)  #实例化工厂类
        yield
        time.sleep(3)
        self.driver.quit()

   def test_xun_chen(self):
        # 击击稍后更新
        # self.factor_page.index_page().base_click_element()
        #我的 按钮
        self.factor_page.index_page().click_mine()
        # 登录按钮码
        self.factor_page.login_page().click_login_reg()
        # 输入手机号码
        # self.factor_page.mine_page().input_phone_log("13288834897")
        # # 输入密码
        # self.factor_page.mine_page().input_pwd_log("13288834897")
        # # 点击登录
        # self.factor_page.mine_page().click_log()
        # #点击确认
        # self.factor_page.mine_page().click_confirm_btn()
        self.factor_page.mine_page().account_login("13288834897","13288834897")
