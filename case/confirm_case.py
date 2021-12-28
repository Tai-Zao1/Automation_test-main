#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "千随"
__title__ = "内容闯关"
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import threading
from page.LOGIN_Page.start_page import StartAPP
from page.LOGIN_Page.login_page import UserLogin
from page.Game_Page.confirm_page import Confirm
from page.Home_Page.new_home_page import HomePage
from page.Search_Page.search_page import search_page
from tool.Generate_log import Tool
import unittest
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
            UserLogin().test1_login(2, "19901679570", "123456")
            HomePage().test4_search()
            search_page().test1_search("完美日记探险家十二色眼影动物眼影盘")
            HomePage().test1swipeFB(".*十二色眼影动物眼.*", 1)
            Confirm().test1_confirm_answer("Discovery频道", "完美日记心动代言人，刘宇", "眼影粉", "四种质地都包含", "镜鲤盘", "P与D并列平行放置", "全部正确")
        finally:
            # 生成测试报告
            Tool().test2loggin_html()


if __name__ == "__main__":
    from tool.phone_devices import devicestest

    devicestest().parallel(newtest.run_script)
