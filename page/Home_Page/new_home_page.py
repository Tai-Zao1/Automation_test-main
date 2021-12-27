# -*- encoding=GBK -*-
import logging

__author__ = "千随"
__title__ = "首页"

from time import  time
import unittest
from page.Search_Page.search_page import search_page
from airtest.core.api import *

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)
time_now = time.strftime("%Y%m%d-%H%M%S", time.localtime())

class HomePage(unittest.TestCase):

    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    # 刷新列表，找到某个活动并进入

    def test1swipeFB(self, Fbname, Type):  # Fbname:活动名称
        # type= 1：大牌免费拿，2：指间剧场or短视频
        time.sleep(2)
        search = self.poco(name="com.devkeep.mall:id/tv_search")
        while len(self.poco(text="可能感兴趣的人")) != 1 and len(search) != 1:
            swipe([550, 400], [550, 1700])
            print("-------正在滑动到顶部-------")
        else:
            swipe([550, 400], [550, 1700])
            print("---------------刷新内容列表-----------------")
        time.sleep(2)
        while len(self.poco(name="com.devkeep.mall:id/tv_name", textMatches=Fbname)) != 1:
            swipe([500, 903], [500, 150])
            print("正在滑动找到该活动")
        if Type == 1:
            print("---------------找到该大牌活动---------------")
            # snapshot(filename=time, msg="滑动找到活动")
            find_1 = self.poco(
                nameMatches="com.devkeep.mall:id/include_type4.*?")
            assert_equal(find_1.exists(), True, "大牌活动入口")
            find_1[-1].click()
        elif Type == 2:
            print("---------------找到该指间剧场or短视频活动---------------")
            find_2 = self.poco(
                name="com.devkeep.mall:id/iv_advert_interactive")
            assert_equal(find_2.exists(), True, "指间剧场or短视频活动入口")
            find_2[-1].click()
        else:
            print("---------------没有找到该活动---------------")

    # 关注按钮

    def test2_attention(self):
        creator_name = self.poco(
            name="com.devkeep.mall:id/tv_author")[-1].get_text()
        attention = self.poco(name="com.devkeep.mall:id/btn_attention")[-1]
        if attention.get_text() == "关注":
            attention.click()
            print("点击关注该创作者:" + creator_name)
        else:
            print("按钮状态:" + attention.get_text())

    # 内容评论

    def test3_comment(self, name, commenttext):  # name = 活动名称，commenttext = 输入内容
        comment_button = self.poco(textMatches=".*?" + name + ".*?")[-1].sibling(
            "com.devkeep.mall:id/ll_comment").offspring("com.devkeep.mall:id/et_comment")
        while len(comment_button) != 1:
            swipe([500, 700], [500, 300])
        else:
            comment_button.set_text(commenttext)
            device().yosemite_ime.code("4")

    # 搜索
    def test4_search(self):
        search = self.poco(name="com.devkeep.mall:id/xTablayout").sibling(name="android.widget.ImageView")
        search.click()
        return search_page

    # def test5_give_like(self):
    # 暂时无法判断是否是已点赞状态


if __name__ == "__main__":
    unittest.main()
