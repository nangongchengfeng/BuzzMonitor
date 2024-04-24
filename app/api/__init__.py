# -*- coding: utf-8 -*-
# @Time    : 2024-04-24 11:31
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : __init__.py.py
# @Software: PyCharm
from app.api.rep_info import info

DEFAULT_BLUEPRINT = [
    (info, '/info'),
]

def config_blueprint(app):
    for blueprint, url_prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=url_prefix)