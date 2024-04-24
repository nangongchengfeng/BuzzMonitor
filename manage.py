# -*- coding: utf-8 -*-
# @Time    : 2024-04-24 11:25
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : app.py
# @Software: PyCharm
from app import create_app

# 默认为开发环境，按需求修改
config_name = 'development'

app = create_app(config_name)

if __name__ == '__main__':
    app.run()