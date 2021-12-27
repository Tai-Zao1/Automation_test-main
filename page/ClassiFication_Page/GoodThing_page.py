# -*- encoding=GBK -*-
__author__ = "孙志宇"
__title__ = "好物页面"

import unittest

import logging
from page.Card_Page.shoppingcard_page import ShoppingCard
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)



class GoodThing(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.poco = poco

    # 点击好物按钮
    def test1_classification(self):
        # 点击按钮
        self.poco(text="好物").click()

    # 点击搜索框并输入商品名
    def test2_search_et(self, TradeName):
        self.poco(name="com.devkeep.mall:id/search_et").click()
        self.poco(name="com.devkeep.mall:id/search_et").set_text(TradeName)
        self.poco(name="com.devkeep.mall:id/search_btn").click()
        # 判断上面搜索商品是否存在
        if TradeName in self.poco(name="com.devkeep.mall:id/goods_name")[0].get_text():
            self.poco(name="com.devkeep.mall:id/cart_iv")[0].click()
            # 判断商品是否有sku
            if len(self.poco(name="com.devkeep.mall:id/tag_tv")) >= 1:
                self.poco(name="com.devkeep.mall:id/tag_tv")[0].click()
                self.poco(name="com.devkeep.mall:id/cart_buy_tv").click()
            else:
                print("----商品没改sku----")
            print("----搜索商品存在并加入购物车----")
        else:
            print("----搜索商品不存在----")

    def test3_shoppingCard_bubble(self):
        self.poco(name="android.widget.ImageView").click()
        return ShoppingCard


if __name__ == "__main__":
    unittest.main()
