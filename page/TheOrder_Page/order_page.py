#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "孙志�?"
__title__ = "确认订单页面"
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


import unittest

from airtest.core.api import *
import logging
from page.My_Page.address_page import Address

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


# noinspection PyTypeChecker
class Order(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.poco = poco

    # 确认收货地址
    def test1_address(self):
        if len(self.poco(name="com.devkeep.mall:id/tv_add_address")) == 1:
            self.poco(name="com.devkeep.mall:id/tv_add_address").click()
            Address().test1_new_address('王大�?', '19901679570', '人民�?')
        else:
            print('----已经有收货地�?----')

    # 获取实付金额
    def test2_amount(self):
        global total_amount
        total_amount = self.poco("android.widget.RelativeLayout") \
            .child("com.devkeep.mall:id/rl_bottom") \
            .offspring("com.devkeep.mall:id/tv_total_amount")

    # 确认支付使用非微信�?�支付宝支付
    def test3_select_payment_type(self):
        # 判断是否有支付金
        aa = str(self.poco("com.devkeep.mall:id/tv_payment").exists())
        if aa == "True":
            self.poco(name="com.devkeep.mall:id/sb_payment").click()
            tv_paymen = self.poco(name="com.devkeep.mall:id/tv_payment").get_text()
            Order().test2_amount()
            print("----选择支付金支�?,支付金额=", tv_paymen, "剩余应付金额 =", total_amount.get_text(), "----")
        else:
            print("----没有支付金或者实付金额为0----")
        # 判断是否有互动奖金且合计金额大于0
        bb = str(self.poco("com.devkeep.mall:id/tv_interactive_amount").exists())
        if bb == "True":
            self.poco(name="com.devkeep.mall:id/sb_interactive_amount").click()
            tv_interactive_amount = self.poco(name="com.devkeep.mall:id/tv_interactive_amount").get_text()
            Order().test2_amount()
            print("----选择互动奖金支付,支付金额=", tv_interactive_amount, "剩余应付金额 =", total_amount.get_text(), "----")
        else:
            print("----没有互动奖金或�?�实付金额为0----")
        # 判断是否有余额且合计金额大于0
        cc = self.poco(name="com.devkeep.mall:id/tv_balance_deduction")
        if str(cc) == "True":
            self.poco(name="com.devkeep.mall:id/sb_balance_deduction").click()
            tv_balance_deduction = self.poco(name="com.devkeep.mall:id/tv_balance_deduction").get_text()
            Order().test2_amount()
            print("----选择余额支付,支付金额=", tv_balance_deduction, "剩余应付金额 =", total_amount.get_text(), "----")
        else:
            print('----没有余额或�?�实付金额为0----')
        # 判断抵扣完应付金额是否大�?0
        Order().test2_amount()
        if total_amount.get_text() != "¥ 0.00":
            print("----没有钱了，剩余应付金�?", total_amount.get_text(), "----")
        else:
            print("----已经全部抵扣----")
            self.poco(name="com.devkeep.mall:id/btn_pay").click()
            print("----进入支付成功页面----")

    # 点击进入第一个店铺详�?
    def test4_supplier(self):
        self.poco(name="com.devkeep.mall:id/rl_supplier")[0].click()

    def test5_wxpay(self):
        self.poco(name="com.devkeep.mall:id/btn_pay").click()
        self.poco(name="com.devkeep.mall:id/weixin_cb").click()
        self.poco(text="确认支付").click()
        time.sleep(2)


if __name__ == "__main__":
    unittest.main()


    # 确认收货地址
    def test1_address(self):
        if len(self.poco(name="com.devkeep.mall:id/tv_add_address")) == 1:
            self.poco(name="com.devkeep.mall:id/tv_add_address").click()
            Address().test1_new_address('王大�?', '19901679570', '人民�?')
        else:
            print('----已经有收货地�?----')


    # 获取实付金额
    def test2_amount(self):
        global total_amount
        total_amount = self.poco("android.widget.RelativeLayout") \
            .child("com.devkeep.mall:id/rl_bottom") \
            .offspring("com.devkeep.mall:id/tv_total_amount")


    # 确认支付使用非微信�?�支付宝支付
    def test3_select_payment_type(self):
        # 判断是否有支付金
        aa = str(self.poco("com.devkeep.mall:id/tv_payment").exists())
        if aa == "True":
            self.poco(name="com.devkeep.mall:id/sb_payment").click()
            tv_paymen = self.poco(name="com.devkeep.mall:id/tv_payment").get_text()
            Order().test2_amount()
            print("----选择支付金支�?,支付金额=", tv_paymen, "剩余应付金额 =", total_amount.get_text(), "----")
        else:
            print("----没有支付金或者实付金额为0----")
        # 判断是否有互动奖金且合计金额大于0
        bb = str(self.poco("com.devkeep.mall:id/tv_interactive_amount").exists())
        if bb == "True":
            self.poco(name="com.devkeep.mall:id/sb_interactive_amount").click()
            tv_interactive_amount = self.poco(name="com.devkeep.mall:id/tv_interactive_amount").get_text()
            Order().test2_amount()
            print("----选择互动奖金支付,支付金额=", tv_interactive_amount, "剩余应付金额 =", total_amount.get_text(), "----")
        else:
            print("----没有互动奖金或�?�实付金额为0----")
        # 判断是否有余额且合计金额大于0
        cc = self.poco(name="com.devkeep.mall:id/tv_balance_deduction")
        if len(cc) == 1:
            if cc.get_text() != "¥0.00":
                self.poco(name="com.devkeep.mall:id/sb_balance_deduction").click()
                tv_balance_deduction = self.poco(name="com.devkeep.mall:id/tv_balance_deduction").get_text()
                Order().test2_amount()
                print("----选择余额支付,支付金额=", tv_balance_deduction, "剩余应付金额 =", total_amount.get_text(), "----")
            else:
                print('----没有余额或�?�实付金额为0----')
        else:
            return
        # 判断抵扣完应付金额是否大�?0
        Order().test2_amount()
        if total_amount.get_text() != "¥ 0.00":
            print("----没有钱了，剩余应付金�?", total_amount.get_text(), "----")
        else:
            print("----已经全部抵扣----")
            self.poco(name="com.devkeep.mall:id/btn_pay").click()
            print("----进入支付成功页面----")


    # 点击进入第一个店铺详�?
    def test4_supplier(self):
        self.poco(name="com.devkeep.mall:id/rl_supplier")[0].click()


    def test5_wxpay(self):
        self.poco(name="com.devkeep.mall:id/btn_pay").click()
        self.poco(name="com.devkeep.mall:id/weixin_cb").click()
        self.poco(text="确认支付").click()
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()
