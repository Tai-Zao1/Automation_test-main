# -*- encoding=utf8 -*-
__author__ = "千随"
__title__ = "登陆流程"

import time
import unittest
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco()
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class Theater(unittest.TestCase):
    def __init__(self):
        unittest.TestCase.__init__(self)
        self.poco = poco
 #指间剧场
    def test1_theater_game(self):
        # if len(self.poco(name= "点击任意处继续")) >=1 :
        #     self.poco(name="点击任意处继续").click()
        # else:
        #     print("剧场已经有历史内容")
        while self.poco(nameMatches = "android.widget.Toast").get_text() == '千随：观看视频可能有奖励哦··················':
            self.poco(name= "android.widget.Button").click()
        else:
            self.poco.click([0.5,0.8])


#闯关赢大奖活动
    def test2_answer(self,answers):
        complete = poco(nameMatches="完成.*?")
        again = poco(nameMatches="重新挑战.*?")
        while len(complete) != 1 and len(again) != 1:
            answer = poco(nameMatches=answers+".*?")
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