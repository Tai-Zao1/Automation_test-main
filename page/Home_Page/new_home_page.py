# -*- encoding=utf8 -*-
import logging
__author__ = "千随"
__title__ = "首页"

import time
import unittest
from airtest.core.api import swipe
from airtest.core.api import *
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class HomePage(unittest.TestCase):

    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    # 刷新列表，找到某个活动并进入

    def test1swipeFB(self, Fbname, Type):  # Fbname:活动名称
        # type= 1：大牌免费拿，2：指间剧场or短视频
        time.sleep(2)
        while len(self.poco(text="可能感兴趣的人")) != 1:
            swipe([550, 400], [550, 1700])
            print("-------正在滑动到顶部-------")
        else:
            swipe([550, 400], [550, 1700])
            print("---------------刷新内容列表-----------------")
        while len(self.poco(textMatches=Fbname)) != 1:
            swipe([500, 903], [500, 150])
            print("正在滑动找到该活动")
        if Type == 1:
            print("---------------找到该大牌活动---------------")
            find_1 = self.poco(
                nameMatches="com.devkeep.mall:id/include_type4.*?")
            assert_equal(find_1.exists(), True, "大牌活动入口")
            find_1[-1].click()
        elif Type == 2:
            print("---------------找到该指间剧场or短视频活动---------------")
            find_2 = self.poco(
                name="com.devkeep.mall:id/iv_advert_interactive")
            assert_equal(find_2.exists(), True, "指间剧场or短视频活动入口")
            find_2[-1].click()
        else:
            print("---------------没有找到该活动---------------")


if __name__ == "__main__":
    unittest.main()
