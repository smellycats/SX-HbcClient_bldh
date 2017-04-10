# -*- coding: utf-8 -*-
import json

import requests
from requests.auth import HTTPBasicAuth


class Kakou(object):
    def __init__(self, **kwargs):
        self.host = kwargs['host']
        self.port = kwargs['port']
	self.city = kwargs['city']
	self.username = kwargs['username']
	self.password = kwargs['password']
        self.headers = {'content-type': 'application/json'}

	self.status = False

    def get_kkdd(self, kkdd_id):
        """获取卡口地点"""
        url = 'http://{0}:{1}/kk/{2}/kkdd/{3}'.format(
            self.host, self.port, self.city, kkdd_id)
        try:
            r = requests.get(url, headers=self.headers,
		 	     auth=HTTPBasicAuth(self.username, self.password))
            if r.status_code == 200:
                return json.loads(r.text)['items']
            else:
                self.status = False
                raise Exception(u'url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
	    self.status = False
            raise

    def get_kkdd_all(self):
        """获取卡口地点"""
        url = 'http://{0}:{1}/kk/{2}/kkdd'.format(
            self.host, self.port, self.city)
        try:
            r = requests.get(url, headers=self.headers,
		 	     auth=HTTPBasicAuth(self.username, self.password))
            if r.status_code == 200:
                return json.loads(r.text)['items']
            else:
                self.status = False
                raise Exception(u'url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
	    self.status = False
            raise

    def get_kakou(self, first_id, last_id):
	"""根据ID范围获取卡口信息"""
        url = 'http://{0}:{1}/kk/{2}/kakou/{3}/{4}'.format(
            self.host, self.port, self.city, first_id, last_id)
        try:
            r = requests.get(url, headers=self.headers,
			     auth=HTTPBasicAuth(self.username, self.password))
            if r.status_code == 200:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception(u'url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
            self.status = False
            raise

