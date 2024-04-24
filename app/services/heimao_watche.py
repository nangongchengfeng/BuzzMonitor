# -*- coding: utf-8 -*-
# @Time    : 2024-04-24 14:00
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : heimao_watche.py
# @Software: PyCharm
import hashlib
import json
import random
import time
import uuid
import requests

import app
from app.config import KEYWORDS
from app.utils.LogHandler import log
from app.utils.date_tool import getStrTime

header = {
    # 'Referer': 'https://tousu.sina.com.cn/company/view/?couid=6330679669&sid=16754',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}


# 黑猫诉网页爬虫
def resolve_dict(result, keyword):
    try:
        datas = result['data']
        if datas and datas['complaints']:
            postList = datas['complaints']
            # logger.info('黑猫爬取数据长度 len(postList)=%s', len(postList))
            data = []
            for lists in postList:
                try:
                    main_data = lists['main']
                    author_data = lists['author']
                    title = main_data['title']
                    title = title.replace('<span class="code-red">', '').replace('</span>', '') if title else title
                    cotitle = main_data['cotitle']
                    cotitle = cotitle.replace('<span class="code-red">', '').replace('</span>',
                                                                                     '') if cotitle else cotitle
                    content = main_data['summary']
                    if title and content:
                        field = {
                            "_id": str(uuid.uuid1()),
                            'source': '黑猫投诉',
                            'keyword': keyword,
                            'url': 'https:' + str(main_data['url']),
                            'title': title,
                            'content': content,
                            'complaint_claim': main_data['appeal'],
                            'complaint_obj': cotitle,
                            'author': author_data.get('title'),
                            # 'time_stamp': main_data['timestamp'],
                            'exist_date': getStrTime(int(main_data['created_at'])),
                            'time_stamp': int(main_data['created_at']),
                            'query_date': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
                            # 'analy': getHit('{}-{}'.format(title, content))
                            'analy': '负面'

                        }
                        data.append(field)
                except Exception as e:
                    log.exception(e)
                    continue
            log.info('黑猫解析后数据长度 len(data)=%s', len(data))
            # ids = keep_data(data)
            # print(ids)
            # logger.info('黑猫投诉成功入库ids=%s', ids)
            # print(data)
        else:
            log.exception('解析数据失败，errorCode=%s', (result['status']))
    except Exception as e:
        log.exception(e)


def get_sha256(value):
    """
    sha256加密
    :param value: 加密字符串
    :return: 加密结果转换为16进制字符串，并大写
    """
    hsobj = hashlib.sha256()
    hsobj.update(value.encode("utf-8"))
    return hsobj.hexdigest()


def req_heimao(keyword, page=1):
    # 获取当前时间的13位时间戳
    p = str(int(time.time() * 1000))

    # 可选择的字符集，用于生成随机字符串
    a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
         "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H",
         "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    # 生成一个16字符长的随机字符串
    b = ''.join(random.choice(a) for i in range(16))

    # 固定字符串，可能用于加密过程的一部分
    y = '$d6eb7ff91ee257475%'

    # 将整数10转换为字符串，可能用于请求参数
    h = str(10)

    # 将页码参数转换为字符串
    page = str(page)

    # 默认请求类型参数，转换为字符串
    type = str(1)

    # 计算签名所需的各个组成部分
    ts = p
    rs = b
    # 签名组成：将提供的参数与生成的字符串按顺序排序后进行哈希
    signature = ''.join(sorted([p, b, y, keyword, type, h, page]))
    signature = hashlib.sha256(signature.encode('utf-8')).hexdigest()

    try:
        log.info('开始黑猫投诉论坛数据抓取，关键词keyword=%s', keyword)
        # keywords = parse.quote_plus(keyword)
        url = f'https://tousu.sina.com.cn/api/company/received_complaints?' \
              f'ts={ts}&rs={rs}&signature={signature}' \
              f'&type=1&page_size=10&page={page}&couid={keyword}'
        # print(url)
        html = requests.get(url, headers=header)  # , verify=False, allow_redirects=False
        cat_dict = json.loads(html.text)
        result = cat_dict['result']
        return result
    except Exception as e:
        log.exception(e)


def get_heimao():
    # 使用关键字
    for keyword in KEYWORDS:
        resolve_dict(req_heimao(keyword), keyword)


if __name__ == '__main__':
    get_heimao()
