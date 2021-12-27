# -*- encoding=GBK -*-
__author__ = "孙志宇"
__title__ = "购物车列表"

from airtest.core.api import *
import unittest

from page.TheOrder_Page.order_page import Order
import logging

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)




class ShoppingCard(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.poco = poco

    # 点击购物车按钮
    def test_card(self):
        self.poco(text="购物车").click()

    # 商品数量加
    def test1_add(self):
        if len(self.poco(name="com.devkeep.mall:id/plus")) >= 1:
            add = self.poco(name="com.devkeep.mall:id/plus")[0]  # 下标是0的第一个商品加
            add.click()
            print("----购物车第一个商品数量+1----")
        else:
            print("----购物车没有商品----")

    # 商品数量减
    def test2_minus(self):
        if len(self.poco(name="com.devkeep.mall:id/cart_item_rv")[0]) >= 1 \
                and int(self.poco(name="com.devkeep.mall:id/goods_count")[0].get_text()) > 1:  # 判断有商品且第一商品数量大于1
            minus = self.poco(name="com.devkeep.mall:id/minus")[0]  # 下标是0的第一个商品
            minus.click()
            print("----第一个商品数量-1----")
        else:
            print("----购物车没有商品----")

    # 删除所有商品
    def test3_delete(self):
        while len(self.poco(name="com.devkeep.mall:id/cart_item_rv")) >= 1:
            productName = self.poco(name='com.devkeep.mall:id/des')[0].get_text()
            # self.poco.swipe([0.8, 0.22], [0.3, 0.22])  # 第一个商品的坐标比例
            cart_item_position = self.poco(name = "com.devkeep.mall:id/cart_item_rv")[0].get_position()
            x,y = cart_item_position[0],cart_item_position[1]
            self.poco.swipe([x,y],[x-0.4,y])
            time.sleep(0.5)
            # aa = self.poco("com.devkeep.mall:id/delete")[0].exists()
            # print(aa)
            # self.poco("com.devkeep.mall:id/delete").exists()
            self.poco(name="com.devkeep.mall:id/delete")[0].click()
            time.sleep(0.5)
            self.poco(name="com.devkeep.mall:id/confirm").click()
            print("删除购物车商品",productName)
        else:
            print("----购物车没有商品或者全部已删除----")



    # 点击去逛逛
    def test4_goshopping(self):
        if len(self.poco(name='com.devkeep.mall:id/tohomePage')) >= 1:
            sp = self.poco(name='com.devkeep.mall:id/tohomePage')
            sp.click()
            print("----去逛逛----")
        else:
            print("----购物车有商品没有<去逛逛按钮>----")

    # 点击去结算
    def test5_pay(self):
        # 刷新确保商品选中
        swipe([0.51, 0.18], [0.51, 0.65])
        if len(self.poco(name='com.devkeep.mall:id/cart_item_rv')) >= 1:
            # self.poco(name="com.devkeep.mall:id/all_check").click() #点击全选按钮
            self.poco(name='com.devkeep.mall:id/pay').click()
            print("----进入确认订单页面----")
            return Order

        else:
            print("----购物车没有商品不可以下单----")


if __name__ == '__main__':
    unittest.main()
