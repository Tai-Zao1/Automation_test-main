# -*- encoding=utf8 -*-
import logging
__author__ = "千随"
__title__ = "游戏化内容"

import time
import unittest
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco()
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class Theater(unittest.TestCase):
    def __init__(self):
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
                    ss = poco("android:id/content").child("android.widget.FrameLayout").child(
                        "android.widget.FrameLayout").child("android.view.View").child("android.view.View").child(
                        "android.view.View").child("android.view.View").child("android.widget.ImageView")[1]
                    ss.click()
                    time.sleep(3)
                else:
                    break

    # 闯关赢大奖活动
    def test2_answer(self, answers):
        complete = poco(nameMatches="完成.*?")
        again = poco(nameMatches="重新挑战.*?")
        while len(complete) != 1 and len(again) != 1:
            answer = poco(nameMatches=answers + ".*?")
            next_title = poco(nameMatches="下一题.*?")
            if len(answer) != 0:
                answer.click()
            elif len(next_title) == 1:
                next_title.click()
        else:
            if len(complete) == 1:
                print("---------------完成答题---------------")
            else:
                print("---------------答题出错---------------")


if __name__ == "__main__":
    unittest.main()
