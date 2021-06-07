# -*- encoding=utf8 -*-
import logging
__author__ = "千随"
__title__ = "首页"

import time
import unittest

from airtest.core.api import swipe
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco()
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class HomePage(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.poco = poco

    # 刷新列表，找到某个活动并进入

    def test1swipeFB(self, Fbname):
        while len(poco(text="可能感兴趣的人")) != 1:
            swipe([550, 400], [550, 1700])
        else:
            swipe([550, 400], [550, 1700])
            print("---------------刷新内容列表-----------------")
        while len(poco(text=Fbname)) != 1:
            swipe([500, 903], [500, 150])
        else:
            print("---------------找到该活动---------------")
            poco(name="com.devkeep.mall:id/include_type4")[-1].click()


if __name__ == "__main__":
    unittest.main()
