# -*- coding: utf-8 -*-
# @Time    : 2023/12/12 11:06
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : databaseModel.py
# @Software: PyCharm
from datetime import datetime

from app import db
from app.models.CatModel import CatModels
from manage import app
# 假设 data 是接收到的字典数据
data = {
    '_id': '1939dcb7-0206-11ef-956f-047f0e2017ee',
    'sn': '17372711541',
    'source': '黑猫投诉',
    'keyword': '6330679669',
    'url': 'https://tousu.sina.com.cn/complaint/view/17372711541/',
    'title': '富宝贷暴力催收',
    'content': '富宝贷平台，暴力催收。很多电话轰炸我 富宝贷平台暴力催收。一天打好多电话。和短信。联系得上我本人情况下也去联系联系人,本人并非恶意欠款不还，本人失业没有工作',
    'complaint_claim': '停止骚扰,道歉赔偿/解释',
    'complaint_obj': '富宝袋',
    'author': '',
    'exist_date': '2024-04-23 11:48:38',
    'time_stamp': 1713844118,
    'query_date': '2024-04-24 14:44:28',
    'analy': '负面'
}


if __name__ == '__main__':

    # with app.app_context():
    #     # 查询所有中间件数据
    #     middlewares = CatModels.query.all()
    #     # 将结果转换为字典列表（或其他您需要的格式）
    #     # 检查数据库中是否已存在相同id的记录
    #     existing_complaint = db.session.query(CatModels).filter_by(sn=data['sn']).first()
    #     print(existing_complaint)
    #     if not existing_complaint:
    #         new_complaint = CatModels(
    #             id=data['_id'],
    #             sn=data['sn'],
    #             source=data['source'],
    #             keyword=data['keyword'],
    #             url=data['url'],
    #             title=data['title'],
    #             content=data['content'],
    #             complaint_claim=data['complaint_claim'],
    #             complaint_obj=data['complaint_obj'],
    #             author=data['author'],
    #             exist_date=datetime.strptime(data['exist_date'], '%Y-%m-%d %H:%M:%S'),
    #             time_stamp=data['time_stamp'],
    #             query_date=datetime.strptime(data['query_date'], '%Y-%m-%d %H:%M:%S'),
    #             analy=data['analy']
    #         )
    #         db.session.add(new_complaint)
    #         db.session.commit()
    #     else:
    #         print("Record already exists and was not added.")

    with app.app_context():
        try:
            # 默认值
            page = 1
            per_page = 10

            # 分页查询
            pagination = CatModels.query.paginate(page=page, per_page=per_page, error_out=False)
            middlewares = pagination.items

            # 构建响应数据
            data = {
                'data': [{'id': mw.id, 'content': mw.content} for mw in middlewares],
                'total': pagination.total,
                'pages': pagination.pages,
                'current_page': pagination.page
            }
            print(data)
        except Exception as e:
            print(e)