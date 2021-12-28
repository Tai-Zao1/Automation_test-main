#!/usr/bin/python
# -*-coding:GBK -*-
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


from multiprocessing.context import Process
import unittest
from airtest.core.android.adb import ADB


class devicestest(unittest.TestCase):
    def get_devices(self):
        '''获取设备'''
        devicesList = ADB().devices()
        return devicesList

    def parallel(self, case):
        dev = []
        for i in devicestest().get_devices():
            dev.append(Process(target=case, args=(i[0],)))
        for p in dev:
            p.start()
        for p in dev:
            p.join()


if __name__ == "__main__":
    unittest.main()
