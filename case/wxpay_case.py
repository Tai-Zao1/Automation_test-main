#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "孙志宇"
__title__ = "微信支付流程"
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import threading
import unittest
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import logging
from airtest.core.api import wake
from tool.Generate_log import Tool

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)
poco = AndroidUiautomationPoco()

from page.WX_Page.WX_page import weixin_page
from page.LOGIN_Page.start_page import StartAPP
from page.LOGIN_Page.login_page import UserLogin
from page.ClassiFication_Page.GoodThing_page import GoodThing
from page.Card_Page.shoppingcard_page import ShoppingCard
from page.TheOrder_Page.order_page import Order


class wx_pay_case(threading.Thread):

    def test1_wx_pay(devices):

        try:
            Tool().test1loggin(devices)
            # 页面截图
            wake()
            # 初始化设备
            StartAPP().clearapp()
            StartAPP().test1_start()
            StartAPP().test2_update_app()
            # 登录
            UserLogin().test1_login("19901679570", "123456")
            UserLogin().test2_red_envelopes()
            # 先删除购物车所有商品
            ShoppingCard().test_card()
            ShoppingCard().test3_delete()
            # 进入分类搜索上坡加入购物车
            GoodThing().test1_classification()
            GoodThing().test2_search_et("macbook")
            GoodThing().test3_shoppingCard_bubble()
            # 进入购物车页面
            ShoppingCard().test1_add()
            ShoppingCard().test5_pay()
            # 进入确认订单页面
            Order().test1_address()
            Order().test2_amount()
            # 微信支付进入
            Order().test5_wxpay()
            # 输入微信支付密码
            weixin_page().test1_wxpay('112233')
        finally:
            # 生成测试报告
            Tool().test2loggin_html()


if __name__ == "__main__":
    from tool.phone_devices import devicestest

    devicestest().parallel(wx_pay_case.test1_wx_pay())
