# -*- encoding=utf8 -*-
__author__ = "千随"
__title__ = "内容闯关"
from page.LOGIN_Page.start_page import StartAPP
from page.LOGIN_Page.login_page import UserLogin
from page.Game_Page.theatre_page import Theater
from page.Home_Page.new_home_page import HomePage
from tool.Generate_log import Tool
import unittest
import logging
from airtest.core.api import wake
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

class newtest(unittest.TestCase):

    def testrun_script(devices):
        """
        执行测试脚本
        :param devices:
        :return:
        """
        Tool().test1loggin(devices)
        # connect_device("android:///" + devices)
        # print(devices)
        wake()
        StartAPP().stopapp()
        UserLogin().test1_login("19901679570", "123456")
        HomePage().test1swipeFB("3.0.1新版闯关赢大奖活动", 1)
        Theater().test2_answer("正确答案")
        # 生成测试报告
        Tool().test2loggin_html()

if __name__ == "__main__":
    from tool.phone_devices import devicestest
    devicestest().parallel(newtest.testrun_script)
