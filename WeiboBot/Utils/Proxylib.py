#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
'''

 * @version: 0.0.0
 * @Company: 
 * @Author: zhanming.zhang 
 * @Date: 2019/11/19 11:48 
 * @Last Modified by:   zhanming.zhang 
 * @Last Modified time: 2019/11/19 11:48
 * @Desc: 
'''


def getProxy():

    import requests
    url = "http://localhost:8000/proxy/api/get_ip_bs?appKey=&format=raw&count=1"

    req = requests.get(url=url)
    return req.json()[0]

def getRandomProxyHTTPS():

    proxy = getProxy()
    return {"https":"https://%s" % proxy}


def getRandomProxyHTTP():

    proxy = getProxy()
    return {"http":"http://%s" % proxy}