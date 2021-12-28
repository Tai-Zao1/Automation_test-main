# -*-coding:GBK -*-

import sys

sys.path.append(sys.path[0] + '\..')

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
