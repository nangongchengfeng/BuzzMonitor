# -*- coding: utf-8 -*-
# @Time    : 2024-04-24 11:38
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : rep_info.py
# @Software: PyCharm
from flask import Blueprint

from app.utils.LogHandler import log

info=Blueprint('info',__name__)


def send_alert():
    log.info("发送告警成功")


@info.route('/')
def get_info():
    log.info("加载配置项成功")
    return 'get_info'