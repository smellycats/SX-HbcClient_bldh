# -*- coding: utf-8 -*-
import time
import datetime
import json

import arrow
import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

from ini_conf import MyIni
#from helper_kakou2 import Kakou
from helper_kakou_bldh import Kakou
from helper_hbc import Hbc


class FetchData(object):

    def __init__(self):
        self.my_ini = MyIni()
        self.kakou_conf = self.my_ini.get_kakou()
        #self.hbc_conf = self.myini.get_hbc()
        self.kakou = Kakou(**self.my_ini.get_kakou())
        self.hbc = Hbc(**self.my_ini.get_hbc())
        
        self.id_flag = self.kakou_conf['id_flag']
        self.step = self.kakou_conf['id_step']
        self.kkdd = self.kakou_conf['kkdd']
        self.city = self.kakou_conf['city']

        self.kakou.status = False
        self.hbc.status = False

    def __del__(self):
        del self.myini


    def set_id(self, _id):
        """设置ID"""
        print self.id_flag
        self.id_flag = _id
        self.my_ini.set_id(_id)

    def fetch_data(self):
        """获取卡口车辆信息"""
        info = self.kakou.get_kakou(self.id_flag+1, self.id_flag+self.step)
        #print info['total_count']
        if info['total_count'] == 0:
            return
        
        # 过滤无效车牌
        def data_valid(i):
            if i['kkdd_id'] and i['hphm'] != '' and i['hphm'] != '-':
                return i
        d = filter(data_valid, info['items'])
        if d:
            r = self.hbc.kakou_post(d)
        self.set_id(info['items'][-1]['id'])
        if len(d) > 5:
            print '{0}: {1}_{2}'.format(arrow.now(), self.city, self.id_flag)

    def main_loop(self):
        while 1:
            if self.kakou.status and self.hbc.status:
                try:
                    self.fetch_data()
                    time.sleep(1)
                except Exception as e:
                    time.sleep(15)
            else:
                try:
                    print self.kakou.status
                    print self.hbc.status
                    if not self.kakou.status:
                        self.kakou.get_kkdd_all()
                        self.kakou.status = True
                    if not self.hbc.status:
                        self.hbc.que_get()
                        self.hbc.status = True
                except Exception as e:
                    time.sleep(1)

if __name__ == '__main__':  # pragma nocover
    fd = FetchData()
    fd.main_loop()
