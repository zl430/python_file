# -*- coding=utf-8 -*-
import requests
import itchat
import random

KEY = '04f44290d4cf462aae8ac563ea7aac16'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
#@itchat.msg_register(['Text','Map', 'Card','Sharing', 'Picture'])
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    robots=['——反正不是本人,爱咋咋地！！']
#    reply = get_response(msg['Text'])+random.choice(robots)
    reply = get_response(msg['Text'])
    return reply or defaultReply

itchat.auto_login(enableCmdQR=True)
itchat.run()
