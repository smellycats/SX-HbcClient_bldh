# -*- coding: utf-8 -*-
import json

import requests
from requests.auth import HTTPBasicAuth


class Hbc(object):
    def __init__(self, **kwargs):
        self.host = kwargs['host']
        self.port = kwargs['port']
        self.headers = {'content-type': 'application/json'}

	self.status = False

    def kakou_post(self, data):
        """上传卡口数据"""
        url = u'http://{0}:{1}/hbc'.format(self.host, self.port)
        try:
            r = requests.post(url, headers=self.headers,
                              data=json.dumps({'carinfo': data}))
            if r.status_code == 202: #or r.status_code == 429:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception('url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
            self.status = False
            raise

    def que_get(self):
        """查看队列情况"""
        url = u'http://{0}:{1}/que'.format(self.host, self.port)
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code == 200:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception('url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
            self.status = False
            raise
