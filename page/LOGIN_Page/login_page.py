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


class UserLogin(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.poco = poco

    # 登陆
    def test1_login(self, username, password):
        time.sleep(1)
        if len(self.poco(name='com.devkeep.mall:id/login')) >= 1:
            lg = self.poco(name='com.devkeep.mall:id/login')
            lg.click()
            self.poco(text='其他号码登录').click()
            self.poco(text='密码登录').click()
            self.poco(name='com.devkeep.mall:id/et_username').set_text(username)
            self.poco(name='com.devkeep.mall:id/et_password').set_text(password)
            time.sleep(0.5)
            self.poco(name='com.devkeep.mall:id/btn_login_in').click()
            print('----登陆成功----')
        else:
            print('----设备已登录----')
        time.sleep(2)
        #     swipe([500,400],[500,1400])   #下拉刷新
        time.sleep(2)

        # 处理奖品弹窗
        while len(self.poco(nameMatches=".*?立即领取")) >= 1:
            close = \
                self.poco("android:id/content").child("android.widget.FrameLayout").child(
                    "android.widget.FrameLayout").child(
                    "android.view.View").child("android.view.View").child("android.view.View").child(
                    "android.view.View").child(
                    "android.widget.ImageView")[0]
            close.click()

        else:
            print("----奖励弹窗关闭----")

    # 关闭首页红包弹窗
    def test2_red_envelopes(self):
        # 查找红包关闭按钮，如果 =1 点击
        while len(
                    self.poco("android:id/content").child(
                        "android.widget.FrameLayout").child("android.widget.FrameLayout").child(
                        "android.view.View").child("android.view.View").child(
                        "android.view.View").child("android.view.View").child(
                        "android.widget.ImageView")
                ) == 1:
            re = self.poco("android:id/content").child("android.widget.FrameLayout").child(
                "android.widget.FrameLayout").child(
                "android.view.View").child("android.view.View").child("android.view.View").child(
                "android.view.View").child(
                "android.widget.ImageView")
            re.click()

        else:
            print("----没有红包或红包弹窗全都关闭----")


if __name__ == '__main__':
    unittest.main()
