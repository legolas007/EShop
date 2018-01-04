#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/1/0001 11:04
# @Author  : Usher
# @File    : yunpian.py
import json
import requests


class YunPian(object):

    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self, code, mobile):
        parmas = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "【EShop】您的验证码是{code}。".format(code=code)
        }

        response = requests.post(self.single_send_url, data=parmas)
        re_dict = json.loads(response.text)
        return re_dict


if __name__ == "__main__":
    yun_pian = YunPian("355f24d2721e610b8cc08c8080ce7a4b")
    yun_pian.send_sms("2017", "13061265981")