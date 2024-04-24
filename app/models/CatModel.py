# -*- coding: utf-8 -*-
# @Time    : 2024-04-24 14:55
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : CatModels.py
# @Software: PyCharm

from app.extension import db


class CatModels(db.Model):
    __tablename__ = 'cat_info'

    id = db.Column(db.String(36), primary_key=True)
    sn = db.Column(db.String(255))
    source = db.Column(db.String(255))
    keyword = db.Column(db.String(255))
    url = db.Column(db.String(255))
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    complaint_claim = db.Column(db.Text)
    complaint_obj = db.Column(db.String(255))
    author = db.Column(db.String(255))
    exist_date = db.Column(db.DateTime)
    time_stamp = db.Column(db.Integer)
    query_date = db.Column(db.DateTime)
    analy = db.Column(db.String(50))

    def __repr__(self):
        return f"<Complaint {self.id}>"
    def to_json(self):
        return {
            'id': self.id,
            'sn': self.sn,
            'source': self.source,
            'keyword': self.keyword,
            'url': self.url,
            'title': self.title,
            'content': self.content,
            'complaint_claim': self.complaint_claim,
            'complaint_obj': self.complaint_obj,
            'author': self.author,
            'exist_date': self.exist_date.strftime('%Y-%m-%d %H:%M:%S') if self.exist_date else None,
            'time_stamp': self.time_stamp,
            'query_date': self.query_date.strftime('%Y-%m-%d %H:%M:%S') if self.query_date else None,
            'analy': self.analy
        }
