# -*- encoding=GBK -*-
import logging
__author__ = "千随"
__title__ = "短视频页面"

import time
import unittest
from  airtest.core.api import *
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class Video(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco

        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    def test1_video_answer(self, answer):
        replay = self.poco(name='重播')
        # 等待短视频播放结束后，重播按钮出现
        replay.wait_for_appearance()
        #点击正确答案 answer
        correct_answer = self.poco(nameMatches=".*?" + answer + ".*?")
        correct_answer.click()
        complete = self.poco(name = "回答正确，恭喜通关")
        try:
            assert_equal(complete.exists(), True, "通关页面出现")
        except Exception as e :
            log(e,desc="报错截图",snapshot=True)

if __name__ == "__main__":
    unittest.main()
