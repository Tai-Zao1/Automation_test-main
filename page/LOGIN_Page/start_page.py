# -*- encoding=utf8 -*-
__author__ = "千随"
__title__ = "打开APP并且进入首页"

from airtest.core.api import *
import unittest

# import logging
# logger = logging.getLogger("airtest")
# logger.setLevel(logging.ERROR)



class StartAPP(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    # 杀死并启动APP
    def clearapp(self):
        clear_app("com.devkeep.mall")
        start_app("com.devkeep.mall")
        time.sleep(2)

    #终止目标应用在设备上的运行
    def stopapp(self):
        stop_app("com.devkeep.mall")
        start_app("com.devkeep.mall")
        time.sleep(2)

    # 首次登陆引导页
    def test1_start(self):

        # 确认协议
        self.poco(name="com.devkeep.mall:id/btn_ok").click()
        sleep(0.5)
        # 滑动引导页 3.0.0版本去除引导页
        # swipe([900, 900], [100, 900])
        # swipe([900, 900], [100, 900])
        # swipe([900, 900], [100, 900])
        # swipe([900, 900], [100, 900])
        # 点击进入按钮
        # self.poco(name='com.devkeep.mall:id/btn_enter').click()
        # 确认系统权限
        self.poco(nameMatches='.*?permission_allow_button').click()
        # 处理首页引导
        while len(self.poco(nameMatches="com.devkeep.mall:id/ic_guide.*?")) >= 1:
            gui = self.poco(nameMatches="com.devkeep.mall:id/ic_guide.*?")
            gui.click()
            time.sleep(1)
        else:
            print("----没有引导页或引导页已处理----")

    # 处理升级弹窗问题
    def test2_update_app(self):
        if len(self.poco(name="com.devkeep.mall:id/btn_cancel")) >= 1:
            up = self.poco(name="com.devkeep.mall:id/btn_cancel")
            up.click()
            print("----有新版本升级----")
        else:
            print("----无新版本升级----")


if __name__ == '__main__':
    unittest.main()
