# -*- encoding=utf8 -*-
__author__ = "孙志宇"
__title__ = "微信页面"

import unittest

from airtest.core.api import *
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)



class weixin_page(unittest.TestCase):
    def __init__(self,*args, **kwargs):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self,*args, **kwargs)
        self.poco = poco
    #微信支付（确保已登录）
    def test1_wxpay(self,wxpaypassword):

        if len(self.poco(name= "com.tencent.mm:id/e6k")) == 1 :
            self.poco(name= "com.tencent.mm:id/e6k").click()
            #无法定位密码软键盘，使用adb发送指令
            # shell("imput text '112233'")
            shell("input text " + wxpaypassword)
            #点击返回千随
            self.poco("com.tencent.mm:id/e6k").click()
            print("----微信支付成功----")
            # 返回键

        else:
            # 断言没有登录直接报错
            pay = len(self.poco(name="com.tencent.mm:id/e6k"))
            assert_not_equal(pay,1,"----微信没有登录----")


if __name__ == "__main__":
    unittest.main()