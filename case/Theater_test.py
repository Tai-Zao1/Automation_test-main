# -*- encoding=utf8 -*-
__author__ = "千随"
__title__ = "指间剧场"

# 通用类----------------
import unittest

import logging
from airtest.core.api import *
from airtest.core.api import wake
from tool.Generate_log import Tool
from airtest.core.android.adb import ADB
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

# 通用类----------------


from page.Home_Page.new_home_page import HomePage
from page.Game_Page.theatre_page import Theater
from page.LOGIN_Page.login_page import UserLogin
from page.LOGIN_Page.start_page import StartAPP



class theater_play(unittest.TestCase):

    def test_theater(devices):

        Tool().test1loggin(devices)
        wake()
        StartAPP().stopapp()
        UserLogin().test1_login("19901679570","123456")
        HomePage().test1swipeFB("西游记.*",2)
        Theater().test1_theater_game("选一个你想去的地方","去ktv","就这家了，别BB，怎么去","打车去")
        # 生成测试报告
        # Tool().test2loggin_html()



if __name__ == "__main__":
    from tool.phone_devices import devicestest
    devicestest().parallel(theater_play.test_theater)