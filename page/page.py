# -*- coding=utf-8 -*-
from page.page_home import HomePageAciton
from page.page_myself import MyselfPageAction


class Page:

    def __init__(self,driver):
        self.driver = driver

    def inithomepage(self):
        return HomePageAciton(self.driver)

    def initmyselfpage(self):
        return MyselfPageAction(self.driver)