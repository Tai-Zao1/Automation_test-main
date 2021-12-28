#!/usr/bin/python
# -*-coding:GBK -*-
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


import re

import yagmail
from airtest.cli.parser import cli_setup
from airtest.core.api import *
from airtest.core.api import shell
from airtest.report.report import simple_report
import unittest
import time
# zipfile 用于压缩文件
import zipfile

time_now = time.strftime("%Y%m%d-%H%M", time.localtime())
oldpath = "C:/Users/太早/Desktop/Log/airtest_log/" + time_now


class Tool(unittest.TestCase):

    def test1loggin(self, devices):
        global newdevices
        newdevices = oldpath + "(ip=" + re.sub('[:*?"<>|\r\n]', '-', devices[10:13] + ")")
        if not cli_setup():
            auto_setup(
                __file__,
                logdir=newdevices,
                devices=[
                    "android://127.0.0.1:5037/" +
                    devices +
                    "?cap_method=JAVACAP&&ori_method=MINICAPORI&&touch_method=ADBTOUCH"])
        global devices_name
        devices_name = re.sub(
            '[\\/:*?"<>|\r\n\s]',
            '',
            shell("getprop ro.product.model"))
        return devices_name

    def test2loggin_html(self):
        output1 = newdevices + "/" + devices_name + ".html"
        simple_report(__file__, logpath=True, output=output1)

    def zipDir(self, caseName):
        dirpath = newdevices
        outFullName = newdevices + ".zip"
        zip = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
        for path, dirnames, filenames in os.walk(dirpath):
            # 去掉目标根路径，只对目标文件夹下边的文件及文件夹进行压缩
            fpath = path.replace(dirpath, '')
            for filename in filenames:
                zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
        zip.close()
        # 发送报告
        # 连接邮箱服务器
        yag = yagmail.SMTP(user="sunzhiyu@kilofolo.com", password="Jdke8xLe3z6zVM5f", host='smtp.exmail.qq.com')
        # 邮箱正文，自定义
        contents = ["测试报告:" + devices_name, '用例：' + caseName, '作者：孙志宇']
        # 发送带附件的邮件，最后1个参数为附件地址
        # 接收邮件的邮箱和附件地址可以为列表，即发送给多个邮箱，发送多个附件
        yag.send('sunzhiyu@devkeep.com', '测试报告', contents, [outFullName])


if __name__ == "__main__":
    unittest.main()
