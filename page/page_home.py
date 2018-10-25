import time

from selenium.webdriver.common.by import By

from base.baseaction import BaseAction
class HomePageAciton(BaseAction):
    into_btn_feature = By.ID, "com.tpshop.malls:id/start_Button"
    home_btn_feature = By.XPATH, ("text,首页,1", "resource-id,com.tpshop.malls:id/tab_txtv,1")

    # 给 home 模型定义了一个动作，可以实现自动进入首页的操作
    def auto_enter_home(self):

        time.sleep(3)

        try:
            self.find_element(self.home_btn_feature)
            print("欢迎使用tpshop,进入主界面")
        except Exception:

            for i in range(3):
                self.swipe_left()
                time.sleep(0.6)

            time.sleep(2)
            self.click(self.into_btn_feature)