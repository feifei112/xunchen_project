"""
页面定位元素
"""

from selenium.webdriver.common.by import By

# 学车不 首页面
update_later = (By.XPATH,"//*[contains(@text,'稍后更新')]")  # 点击稍后更新
mine = (By.XPATH,"//*[contains(@text,'我的')]")   # 我的 按钮

# 我的页面
login_reg =(By.ID,"com.bjcsxq.chat.carfriend:id/mine_username_tv")   # 登录按钮

# 登录的页面
phone_log = (By.ID,"com.bjcsxq.chat.carfriend:id/login_phone_et") # 手机号码
pwd_log = (By.ID,"com.bjcsxq.chat.carfriend:id/login_pwd_et") #密码
log = (By.ID,"com.bjcsxq.chat.carfriend:id/login_btn") # 登录
confirm_btn = (By.ID,"com.bjcsxq.chat.carfriend:id/btn_neg ") # 确认




