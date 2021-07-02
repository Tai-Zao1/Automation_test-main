# -*- encoding=utf8 -*-
import logging
__author__ = "千随"
__title__ = "搜索页"

import unittest
from airtest.core.api import *


class search_page(unittest.TestCase):
    def __init__(self,*args,**kwargs):
        unittest.TestCase.__init__(*args,**kwargs)
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        self.poco = poco


    #搜索框
    def test1_search(self,Fbname):
        click_search = self.poco(text = "搜索你感兴趣的内容")
        click_search.click()
        text(Fbname)

    #输出热门搜索
    def test2_hot_search(self):
        hot_search_list = self.poco(name="热门搜索").child(type="android.widget.Button")
        if len(hot_search_list) != 0:
            for i in hot_search_list:
                print("热门搜索："+i.get_name())
        else:
            print(None)

    def test3_history_search(self):
        history_search_list = self.poco(name="历史搜索").child(type="android.widget.Button")
        if len(history_search_list) != 0:
            for i in history_search_list:
                print("历史搜索：" + i.get_name())
        else:
            print("没有历史搜索")



if __name__ == "__main__":
    unittest.main()