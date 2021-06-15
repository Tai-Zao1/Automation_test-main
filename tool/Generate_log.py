from airtest.report.report import simple_report
from airtest.cli.parser import cli_setup
from airtest.core.api import *
import unittest
import time

time_now = time.strftime("%Y%m%d-%H%M", time.localtime())
path = "C:/Users/孙志宇/Desktop/Log/" + time_now


class Tool(unittest.TestCase):
    def test1loggin(self):
        if not cli_setup():
            auto_setup(__file__, logdir=path, devices=[
                       "android://127.0.0.1:5037/192.168.0.100:5555?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=MINITOUCH"])

    def test2loggin_html(self):
        output1 = path + ".html"
        simple_report(__file__, logpath=True, output=output1)


if __name__ == "__main__":
    unittest.main()