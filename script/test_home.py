# -*- coding=utf-8 -*-
from base import initDriver
from page.page import Page
import pytest
pytestmark = pytest.mark.skip( "跳过首页测试" )


class TestDemo:

    def setup(self):
        self.driver = initDriver()
        self.page = Page(self.driver)

    def test_auto_intohome(self):
        self.page.inithomepage().auto_enter_home()

