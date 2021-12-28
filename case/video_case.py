#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "千随"
__title__ = "短视频答题"
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import threading

from page.LOGIN_Page.start_page import StartAPP
from page.LOGIN_Page.login_page import UserLogin
from page.Home_Page.new_home_page import HomePage
from page.Game_Page.video_page import Video
from tool.Generate_log import Tool
import logging
from airtest.core.api import wake

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class newtest(threading.Thread):

    def run_script(devices):
        """
        执行测试脚本
        :param devices:
        :return:
        """
        try:
            Tool().test1loggin(devices)
            wake()
            StartAPP().stopapp()
            UserLogin().test1_login(1)
            HomePage().test1swipeFB("新版视频答题活动", 2)
            Video().test1_video_answer("正确")
        finally:
            # 生成测试报告
            Tool().test2loggin_html()
            Tool().zipDir("短视频答题")


if __name__ == "__main__":
    from tool.phone_devices import devicestest

    devicestest().parallel(newtest.run_script)
