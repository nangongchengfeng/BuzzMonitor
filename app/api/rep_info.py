# -*- coding: utf-8 -*-
# @Time    : 2024-04-24 11:38
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : rep_info.py
# @Software: PyCharm
from flask import Blueprint, jsonify, request, render_template

from app.models.CatModel import CatModels
from app.utils.LogHandler import log

info = Blueprint('info', __name__)


def send_alert():
    log.info("发送告警成功")


@info.route('/')
def index():
    try:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))

        # 分页查询
        pagination = CatModels.query.paginate(page=page, per_page=per_page, error_out=False)
        middlewares = pagination.items

        # 构建响应数据
        data = {
            'data': [
                {'id': mw.id, 'sn': mw.sn, 'source': mw.source, 'keyword': mw.keyword, 'url': mw.url, 'title': mw.title,
                 'content': mw.content, 'complaint_claim': mw.complaint_claim, 'complaint_obj': mw.complaint_obj,
                 'author': mw.author, 'exist_date': mw.exist_date, 'time_stamp': mw.time_stamp,
                 'query_date': mw.query_date,
                 'analy': mw.analy} for mw in middlewares],
            'total': pagination.total,
            'pages': pagination.pages,
            'current_page': pagination.page
        }

        return render_template('index.html', data=data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@info.route('/moniter_info', methods=['POST'])
def get_info():
    # 默认值
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    # 分页查询
    pagination = CatModels.query.paginate(page=page, per_page=per_page, error_out=False)
    middlewares = pagination.items

    # 构建响应数据
    data = {
        'data': [
            {'id': mw.id, 'sn': mw.sn, 'source': mw.source, 'keyword': mw.keyword, 'url': mw.url, 'title': mw.title,
             'content': mw.content, 'complaint_claim': mw.complaint_claim, 'complaint_obj': mw.complaint_obj,
             'author': mw.author, 'exist_date': mw.exist_date, 'time_stamp': mw.time_stamp, 'query_date': mw.query_date,
             'analy': mw.analy} for mw in middlewares],
        'total': pagination.total,
        'pages': pagination.pages,
        'current_page': pagination.page
    }
    return jsonify(data)
