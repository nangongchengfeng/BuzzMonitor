# -*- coding: utf-8 -*-
# @Time    : 2024-04-24 11:38
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : rep_info.py
# @Software: PyCharm
from flask import Blueprint

info=Blueprint('info',__name__)


@info.route('/')
def get_info():
    return 'get_info'