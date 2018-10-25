from base import initDriver
from page.page import Page


class TestDemo:
    def setup(self):
        self.driver = initDriver()
        self.page = Page(self.driver)

    # 定义一个test函数来对应我们测试用例中执行结果为"帐号不存在"的哪一类用例
    def test_login_nonum(self):

        # 使用首页模型当中的进入 首页的动作
        self.page.inithomepage().auto_enter_home()

        # 输入帐号

        # 输入密码

        # 点击登录

        print("我想要测试帐号不存在的哪一类操作")