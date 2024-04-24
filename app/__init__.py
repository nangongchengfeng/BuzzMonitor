# -*- coding: utf-8 -*-
# @Time    : 2024-04-24 11:33
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : __init__.py.py
# @Software: PyCharm
from flask_migrate import Migrate

from app.config import config
from app.extension import db
from app.models import CatModel

def create_app(DevelopmentConfig=None):
    if DevelopmentConfig is None:
        DevelopmentConfig = 'development'
    from flask import Flask
    from app.api import config_blueprint
    from app.extension import config_extensions

    app = Flask(__name__)
    # 加载配置项
    app.config.from_object(config.get(DevelopmentConfig))
    config_blueprint(app)
    config_extensions(app)
    migrate = Migrate(app, db)
    return app