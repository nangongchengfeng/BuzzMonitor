# -*- coding: utf-8 -*-
# @Time    : 2024-04-24 11:25
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : app.py
# @Software: PyCharm
import os
import sys


from app import create_app
from app.utils.LogHandler import log

# 默认为开发环境，按需求修改
config_name = 'development'

app = create_app(config_name)
# 数据库迁移


if __name__ == '__main__':
    # 获取当前文件的绝对路径
    current_file = os.path.abspath(__file__)
    base_dir = os.path.dirname(current_file)
    # 将项目目录添加到 sys.path
    if base_dir not in sys.path:
        sys.path.append(base_dir)
    log.info("启动服务")
    app.run(debug=True, use_reloader=False, threaded=True, host='0.0.0.0', port=5000)