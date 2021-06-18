# -*- encoding=utf8 -*-
__author__ = "孙志宇"
__title__ = "收货地址页面"

import unittest

import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)



class Address(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        self.poco = poco

    def test1_new_address(self, username=None, user_number=None, user_address=None):
        # 收件人
        name = self.poco(name="com.devkeep.mall:id/et_name")
        name.click()
        name.set_text(username)
        # 手机号
        number = self.poco(name="com.devkeep.mall:id/et_phone_number")
        number.click()
        number.set_text(user_number)
        address = self.poco(name="com.devkeep.mall:id/tv_area")
        address.click()
        # 点击确认按钮（地址选择框待优化）
        self.poco(name="com.devkeep.mall:id/btnSubmit").click()
        # 输入详细地址
        detail_address = self.poco(name="com.devkeep.mall:id/et_detail_address")
        detail_address.click()
        detail_address.set_text(user_address)
        # 设为默认
        self.poco(name="com.devkeep.mall:id/cbx_default").click()
        # 保存
        self.poco(name="android.widget.Button").click()


if __name__ == "__main__":
    unittest.main()
