# -*- coding: utf-8 -*-
# @Time    : 2024-04-24 11:33
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : extension.py.py
# @Software: PyCharm
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# 初始化拓展
def config_extensions(app):
    db.init_app(app)
