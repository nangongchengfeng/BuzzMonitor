# -*- coding: utf-8 -*-
# @Time    : 2024-04-24 11:33
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : __init__.py.py
# @Software: PyCharm
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from flask_migrate import Migrate

from app.config import config
from app.extension import db
from app.models import CatModel
from app.services.heimao_watche import get_heimao


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
    # 创建一个后台调度器
    scheduler = BackgroundScheduler(timezone="Asia/Shanghai")
    # 添加一个每隔20秒执行一次的定时任务
    # scheduler.add_job(func=send_alert, trigger="interval", seconds=20)
    # 添加一个每天早上9点执行的定时任务
    scheduler.add_job(func=get_heimao, trigger=CronTrigger(minute='*/10'))
    # 启动调度器
    scheduler.start()
    return app