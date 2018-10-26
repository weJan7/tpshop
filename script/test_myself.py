import time

from base import initDriver
from page.page import Page


class TestDemo:
    def setup(self):
        self.driver = initDriver()
        self.page = Page(self.driver)

    # 定义一个test函数来对应我们测试用例中执行结果为"帐号不存在"的哪一类用例
    def test_login_nonum(self):

        # 使用首页模型当中的进入 首页的动作
        self.page.inithomepage.auto_enter_home()
        self.page.initmyselfpage.click_myself()

        time.sleep(2)  # 涉及到页面转场我们选择停留一定的时间

        # 点击登录注册按钮
        self.page.initmyselfpage.click_login_reg()

        time.sleep(2)

        # 输入帐号
        self.page.initmyselfpage.input_num("13160772173")
        # 输入密码
        self.page.initmyselfpage.input_pwd("123456")
        # 点击登录
        self.page.initmyselfpage.click_enter()

        # 测试登录点击之后的toast 获取
        toast_neirong = self.page.initmyselfpage.get_toast_content()
        # if toast_neirong == "账号不存在!":
        #     # 添加断言
        #     assert 1
        # else:
        #     assert 0

        assert toast_neirong == "账号不存在!"
