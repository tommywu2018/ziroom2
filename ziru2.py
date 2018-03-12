# coding: utf-8

import time
import json
import random
import requests
import webbrowser
import urllib
import pandas as pd

import datetime
import urllib.request



headers0 = {
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'user-agent': 'okhttp/3.9.0',
    'Connection': 'Keep-Alive',
    'Host': 'phoenix.ziroom.com',
    'Accept-Encoding': 'gzip',
    'Accept': 'application/json;version=3',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
    }





def get_answer():
    resp = requests.get('http://phoenix.ziroom.com/v7/room/detail.json?network=4G&sign_open=1&app_version=5.4.5&house_id=26046&sign=4ee275311873a7f045bf4b489fa62126&imei=861365031181741&id=180958&ip=&uid=0&timestamp=1520815932&city_code=110000&os=android%3A5.0.2&model=Redmi+Note+3 HTTP/1.1',headers=headers0,timeout=5).json()
    resp_dict = resp
    resp_dict = eval(str(resp))
    if resp_dict['status'] == 'success':
        if resp_dict['data']['status']=='tzpzz':
            print('room is waiting...')
        else:
            duanxin()
            time.sleep(15+random.random())



def duanxin():
    appkey = 'b9d5501c95ec06b652dcdc7df5956818' #您申请的短信服务appkey
    mobile = '13051168119' #短信接受者的手机号码
    tpl_id = '66349' #申请的短信模板ID,根据实际情况修改 

    sendsms(appkey, mobile, tpl_id) #请求发送短信
 
def sendsms(appkey, mobile, tpl_id):
    sendurl = 'http://v.juhe.cn/sms/send' #短信发送的URL,无需修改 
 
    params = 'key=%s&mobile=%s&tpl_id=%s' % \
             (appkey, mobile, tpl_id) #组合参数
 
    wp = urllib.request.urlopen(sendurl+"?"+params)
    content = wp.read() #获取接口返回内容
 
    result = json.loads(content)
 
    if result:
        error_code = result['error_code']
        if error_code == 0:
            #发送成功
            smsid = result['result']['sid']
            print("sendsms success,smsid: %s" % (smsid))
        else: 
            #发送失败
            print("sendsms error :(%s) %s" % (error_code, result['reason']))
    else:
        #请求失败
        print("request sendsms error")


def main():
    while 1:
        get_answer()
        time.sleep(20+random.random())




if __name__ == '__main__':
    main()
