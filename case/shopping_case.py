# -*- encoding=utf8 -*-
__author__ = "孙志宇"
__title__ = "购物流程"

import threading
import unittest
from airtest.core.api import wake
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import logging
from page.LOGIN_Page.start_page import StartAPP
from page.LOGIN_Page.login_page import UserLogin
from page.ClassiFication_Page.GoodThing_page import GoodThing
from page.Card_Page.shoppingcard_page import ShoppingCard
from page.TheOrder_Page.order_page import Order
from tool.Generate_log import Tool

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)
poco = AndroidUiautomationPoco()


class Shopping_Case(threading.Thread):


    def test1_shopping_case(devices):
        """
        执行测试脚本
        :param aa:
        :return:
        """
        try:
            Tool().test1loggin(devices)
            # 页面截图
            wake()
            StartAPP().clearapp()
            # 初始化设备
            StartAPP().test1_start()
            StartAPP().test2_update_app()
            # 用户登录
            UserLogin().test1_login("19911111111", "123456")
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
            Order().test3_select_payment_type()
        finally:
            # 生成html报告
            Tool().test2loggin_html()


if __name__ == "__main__":
    from tool.phone_devices import devicestest
    devicestest().parallel(Shopping_Case.test1_shopping_case)

