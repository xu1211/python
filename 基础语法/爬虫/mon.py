#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
import requests

gpcode = {
    '上证':'000001',
    '深证':'399001',
    '上证50':'000016',
    '沪深300':'000300',
    '中证500':'000905',
    '50ETF':'510050',
    '300ETF':'510300',
    '500ETF':'510500',
    '':'',
    '':'',
}

if __name__ == '__main__':
    target = 'http://hq.sinajs.cn/list=sh'
    req = requests.get(url=target+gpcode[1])
    print(req.text)