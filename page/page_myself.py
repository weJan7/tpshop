# -*- coding=utf-8 -*-
from selenium.webdriver.common.by import By

from base.baseaction import BaseAction

# 下面这个类里面存放所有 我的 界面模型测试时需要使用的动作
class MyselfPageAction(BaseAction):

    # 将myself界面会用到的元素特征都准备好
    login_reg_feature = By.XPATH,"text,登录/注册,1"
    num_input_feature = By.ID, "com.tpshop.malls:id/edit_phone_num"
    pwd_input_feature = By.ID, "com.tpshop.malls:id/edit_password"
    enter_input_feature = By.ID, "com.tpshop.malls:id/btn_login"

    def click_login_reg(self):
        self.click(self.login_reg_feature)

    def input_num(self,value):
        self.input_txt(self.num_input_feature,value)

    def input_pwd(self,value):
        self.input_txt(self.pwd_input_feature,value)

    def click_enter(self):
        self.click(self.enter_input_feature)


