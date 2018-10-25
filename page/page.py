# -*- coding=utf-8 -*-
from page.page_home import HomePageAciton


class Page:

    def __init__(self,driver):
        self.driver = driver

    def inithomepage(self):
        return HomePageAciton(self.driver)