# -*- coding: utf-8 -*-
# @Time    : 2024-04-24 14:26
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : date_tool.py
# @Software: PyCharm
import time

from app.utils.LogHandler import log


def getStrTime(timeStamp, format='%Y-%m-%d %H:%M:%S'):
    try:
        timeArray = time.localtime(timeStamp)
        otherStyleTime = time.strftime(format, timeArray)
        return otherStyleTime
    except:
        log.info("时间格式转换失败，getStrTime_timeStamp=%s", timeStamp)
        return timeStamp