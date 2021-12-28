# -*- encoding=GBK -*-
import logging

__author__ = "千随"
__title__ = "指间剧场页面"

import sys
sys.path.append(sys.path[0] + '\..')

import unittest
from airtest.core.api import *

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class Theater(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco

        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    # 指间剧场（西游记）flutter页面，需要其他活动请重新编写
    def test1_theater_game(self, one_Q, one_A, two_Q, two_A2):
        while len(self.poco(name="此话已经结束了")) != 1:
            dd = self.poco(name=one_Q)
            ff = self.poco(name=two_Q)
            while len(dd) != 1 and len(ff) != 1:
                self.poco.click([0.5, 0.8])
                # 判断是否是第一个@
                if len(dd) == 1:
                    # 点击第一个A
                    cc = self.poco(name=one_A)
                    cc.click()
                    break
                # 判断是否是第二个Q
                elif len(ff) == 1:
                    # 点击第二个A
                    ee = self.poco(name=two_A2)
                    ee.click()
                    break
                elif len(self.poco(name="恭喜获得宝箱，点击开启")):
                    ss = self.poco("android:id/content").child("android.widget.FrameLayout").child(
                        "android.widget.FrameLayout").child("android.view.View").child("android.view.View").child(
                        "android.view.View").child("android.view.View").child("android.widget.ImageView")[1]
                    ss.click()
                    time.sleep(3)
                else:
                    break


if __name__ == "__main__":
    unittest.main()
