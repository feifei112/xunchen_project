from data.read_data import data_yaml
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
   @pytest.mark.parametrize("phone,pwd,expect",data_yaml())
   def test_xun_chen(self,phone,pwd,expect):
        # 击击稍后更新
        # self.factor_page.index_page().base_click_element()
        #我的 按钮
        self.factor_page.index_page().click_mine()
        # 登录按钮码
        self.factor_page.login_page().click_login_reg()
        # 输入手机号码
        # self.factor_page.mine_page().input_phone_log("13288834897")
        # # 输入密码
        # self.factor_page.mine_page().input_pwd_log("w123456789")
        # # 点击登录
        # self.factor_page.mine_page().click_log()
        # #点击确认
        # self.factor_page.mine_page().click_confirm_btn()
        self.factor_page.mine_page().account_login(phone,pwd)
        user_text = self.factor_page.mine_page().user_name_text()
        assert user_text in expect
