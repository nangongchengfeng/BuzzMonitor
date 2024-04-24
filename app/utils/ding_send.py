# -*- coding: utf-8 -*-
# @Time    : 2024-04-24 16:03
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : ding_send.py.py
# @Software: PyCharm
import base64
import hashlib
import hmac
import json
import time
import urllib.parse

import requests

from app.config import Ding_URl, Ding_SCRET
from app.utils.LogHandler import log


def getDingTalkUrl(url, secret):
    timestamp = str(round(time.time() * 1000))
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc,
                         digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    return url + "&timestamp=" + timestamp + "&sign=" + sign


def sendDingMsg(url,msg):
    # 请求头
    headers = {"Content-Type": "application/json"}

    title = "舆论监控告警"

    # 构建大屏地址
    # big_url = 'http://172.31.161.175:5000'
    # 初始胡文本
    text = f'''<font color=\'#FF0000\'><b>[巡检]</b> </font><b>{title}</b>\n\n --- \n\n'''

    # 处理巡检信息
    # for item in msg:
    text += f'''<font color=\'#778899\' size=2><b>巡检标题：</b> {msg["source"]+ ":"+msg['title']}</font>\n\n '''
    text += f'''<font color=\'#708090\' size=2><b>巡检内容：</b>\n\n内容：{msg['content']}\n\n诉求：{msg['complaint_claim']}\n\n 时间：{msg['query_date']}\n\n 产品：{msg['complaint_obj']}\n\n 影响：{msg['analy']}</font>\n\n\n\n <br> '''
    text += f'''<font color=\'#708090\' size=2><b>详情：</b> [点击查看详情](%s)</font>\n\n ''' % msg["url"]
    text += f'''<font color=\'#778899\' size=2><b>备注：</b> 请及时处理</font>\n\n '''
    # 构建钉钉消息数据
    data = {
        "msgtype": "markdown",
        "markdown": {
            "title": "舆论监控告警",
            "text": text
        }
    }
    # 发送钉钉消息
    res = requests.post(url=url, data=json.dumps(data), headers=headers)
    print("#Send DingTalk robot res:" + str(res.text))
    log.info(f"发送钉钉消息成功:{str(res.text)}")



Ding_Send_Url=getDingTalkUrl(Ding_URl, Ding_SCRET)


if __name__ == '__main__':

    msg = {
	'_id': 'd88fc9c0-0214-11ef-949f-047f0e2017ee',
	'sn': '17372740104',
	'source': '黑猫投诉',
	'keyword': '1003609',
	'url': 'https://tousu.sina.com.cn/complaint/view/17372740104/',
	'title': '客服不退款，也不回复',
	'content': '我在拼多多买的护肤品到货后没拆封不想要了客服不退款也不回复',
	'complaint_claim': '退货退款',
	'complaint_obj': '拼多多客户服务',
	'author': '',
	'exist_date': '2024-04-24 16:00:00',
	'time_stamp': 1713945600,
	'query_date': '2024-04-24 16:30:02',
	'analy': '负面'
}
    url=getDingTalkUrl(Ding_URl, Ding_SCRET)
    sendDingMsg(url,msg)