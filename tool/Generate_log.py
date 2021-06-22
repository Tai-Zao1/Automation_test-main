import re

from airtest.core.android.adb import ADB
from airtest.report.report import simple_report
from airtest.cli.parser import cli_setup
from airtest.core.api import *
from airtest.core.api import shell
from airtest.report.report import simple_report
import unittest
import time
import os


time_now = time.strftime("%Y%m%d-%H%M", time.localtime())
path = "C:/Users/孙志宇/Desktop/Log/" + time_now

class Tool(unittest.TestCase):
    def test1loggin(self, devices):
        global newdevices
        newdevices = path+re.sub('[\/:*?"<>|\r\n]','-',devices)
        if not cli_setup():
            auto_setup(
                __file__,
                logdir=newdevices,
                devices=[
                    "android://127.0.0.1:5037/" +
                    devices +
                    "?cap_method=JAVACAP&&ori_method=MINICAPORI&&touch_method=ADBTOUCH"]
            )
        # connected = print(shell("getprop ro.product.model"),end="")
        # simple_report(__file__, logpath=path+connected)
        # adb = ADB()
        # devices = adb.devices()
        # devicesList = devices
        # devicesNum = len(devicesList) > 1
        # # [('B2T0216822004895', 'device'), ('dce3b005', 'device')]
        # print("本机N个设备，分别是", devicesList)
        # assert_equal(devicesNum, True, "设备连接数量至少为2")
        # for i in range(len(devicesList)):
        #     print(i)
        #     connect_device("android:///" + devicesList[i][0])

    def test2loggin_html(self,):
        connected = shell("getprop ro.product.model")
        # simple_report(__file__, logpath=path + connected)
        output1 = newdevices + ".html"
        simple_report(__file__, logpath=True, output=output1)
        # os.close(newdevices)
        # os.close(output1)


if __name__ == "__main__":
    unittest.main()