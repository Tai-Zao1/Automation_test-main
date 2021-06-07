# -*- encoding=utf8 -*-
__author__ = "千随"
__title__ = "内容闯关"

import time
import unittest


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco()
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)
from page.Home_Page.new_home_page import HomePage
from page.Game_Page.theatre_page import Theater
from page.LOGIN_Page.login_page import UserLogin
from page.LOGIN_Page.start_page import StartAPP

class Play(unittest.TestCase):

    def testfree(self):
        StartAPP().stopapp()
        UserLogin().test1_login("19901679570","123456")
        HomePage().test1swipeFB("3.0.1新版闯关赢大奖活动")
        Theater().test2_answer("正确答案")


if __name__ =="__main__":
    unittest.main()