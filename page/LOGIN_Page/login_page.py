#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "千随"
__title__ = "登陆流程"
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


import time
import unittest

import logging

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class UserLogin(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    # 登陆
    def test1_login(self, type, username=None, password=None):  # type :1 = 多线程（自动获取） ；2 =单线程（手动输入账号密码）
        time.sleep(3)
        login = self.poco(name="com.devkeep.mall:id/login")
        if len(login) >= 1:
            lg = login
            lg.click()
            self.poco(text='其他号码登录').click()
            self.poco(text='密码登录').click()
            from tool.Generate_log import devices_name
            devicesName = devices_name
            print("设备名称：" + devicesName)
            if type == 1:
                if devicesName == "MIX2":
                    self.poco(name='com.devkeep.mall:id/et_username').set_text("19901679570")
                    self.poco(name='com.devkeep.mall:id/et_password').set_text("123456")
                elif devicesName == "MI5s":
                    self.poco(name='com.devkeep.mall:id/et_username').set_text("19901234567")
                    self.poco(name='com.devkeep.mall:id/et_password').set_text("123456")
                else:
                    print("无法识别手机类型")
            elif type == 2:
                self.poco(name='com.devkeep.mall:id/et_username').set_text(username)
                self.poco(name='com.devkeep.mall:id/et_password').set_text(password)
            else:
                print("输入类型错误")
            time.sleep(0.5)
            loginbtn = self.poco(name='com.devkeep.mall:id/btn_login_in')
            loginbtn.click()
            if len(loginbtn) != 1:
                print('----登陆成功----')
            else:
                print('----登陆失败----')
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
