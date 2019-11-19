#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
'''

 * @version: 0.0.0
 * @Company: 
 * @Author: zhanming.zhang 
 * @Date: 2019/11/19 17:23 
 * @Last Modified by:   zhanming.zhang 
 * @Last Modified time: 2019/11/19 17:23
 * @Desc: 
'''

import base64
from WeiboBot.Bot import *
from WeiboBot.WebAPIs.moduleAPI import iconUploadAPI, saveUserInfoAPI, queryUserInfoURI
import os
import requests
class UserInfoMixin:

    @weiboBottle
    def uploadNewIcon(self, uid:str, filebytes:bytes):


        filedata = base64.b64encode(filebytes)
        payload = {"Filedata": filedata,
                   "ax": "79.33333333333334",
                   "ay": "10.833333333333323",
                   "aw": "198.33333333333334",
                   "type": "jpeg",
                   "file_source": "5"}
        headers = {
            'Host': "account.weibo.com",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0",
            'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            'Accept-Language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            'Accept-Encoding': "gzip, deflate, br",
            'Content-Type': "application/x-www-form-urlencoded",
            'Content-Length': str(len(filedata)),
            'Origin': "https://weibo.com",
            'Connection': "keep-alive",
            'Referer': "https://weibo.com/%s/profile?topnav=1&wvr=6&is_all=1" % uid,
            'Cookie': self._getZombieRequestCookie(self.zId),
            'Upgrade-Insecure-Requests': "1",
            'Pragma': "no-cache",
            'Cache-Control': "no-cache",
            'Postman-Token': "f42df093-3d88-491c-826f-46f60b79fe88,ece032b1-5512-456e-84f0-af9432d0bddf",
            'cache-control': "no-cache"
        }

        req = request.FormRequest(
            url=iconUploadAPI.format(int(time.time()*1000)),
            data=payload,
            headers=headers
        )

        resp = self.Fetch.fetch2(
                         method=req.method,
                         url=req.url,
                         data=req.data,
                         headers=req.headers)


        resp.raise_for_status()

        return {"msg":"执行成功",
                "code":200,
                "endTime":int(time.time())}


    @weiboBottle
    def updatePersonalInfo(self,
                           uid:str,
                           gender:str,
                           province:str,
                           city:str,
                           year:str,
                           month:str,
                           day:str,
                           email:str,
                           url:str,
                           qq:str,
                           msn:str,
                           description:str):
        payload = vars()
        del payload['uid']

        headers = self.whichHeaders()
        headers['Referer'] = "https://m.weibo.cn/users/%s?set=1" % uid

        req = request.FormRequest(
            url=saveUserInfoAPI,
            data=payload,
            headers=headers
        )

        resp = self.Fetch.fetch2(
            method=req.method,
            url=req.url,
            data=req.data,
            headers=req.headers
        )
        print(resp.text)
        json_resp = resp.json()
        return self.errCallback(json_resp)


    @weiboBottle
    def queryPersonalInfo(self, uid):

        headers =  {
            'Host': "m.weibo.cn",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0,PostmanRuntime/7.19.0",
            'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8,*/*",
            'Accept-Language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            'Accept-Encoding': "gzip, deflate, br,gzip, deflate",
            'Connection': "keep-alive,keep-alive",
            'Cookie': self._getZombieRequestCookie(self.zId),
            'Pragma': "no-cache",
            'Cache-Control': "no-cache,no-cache",
            'TE': "Trailers",
            }

        req = request.Request(
            method="GET",
            url=queryUserInfoURI.format(uid=uid),
            headers=headers
        )

        resp = self.Fetch.fetch(req)
        print(resp.html().xpath("//p/text()"))

        print(resp.text)