#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
'''

 * @version: 0.0.0
 * @Company: 
 * @Author: zhanming.zhang 
 * @Date: 2019/11/18 11:00 
 * @Last Modified by:   zhanming.zhang 
 * @Last Modified time: 2019/11/18 11:00
 * @Desc: 
'''
import time
import traceback
import urllib.parse
from WeiboBot.Utils.Decorate import weiboBottle
from WeiboBot.WebAPIs.loginAPI import checkLoginStatusAPI
from WeiboBot.WebAPIs.moduleAPI import (createCommentAPI, replyCommentAPI,
                                        postLikeCommentAPI, postLikeMicroblogAPI,
                                        destoryCommentAPI, destoryLikeMicroblogAPI, destoryLikeCommentAPI)

from WeiboBot.RepackHttp.Http import request, response, download


class BotInit:


    def __init__(self,
                 username,
                 password,
                 post_msg,
                 retry_login=5,
                 retry_delay=15,
                 listen=False,
                 proxy_open=False):

        assert isinstance(retry_login, int), "仅能输入正整数"
        self.username = username
        self.password = password
        self.listen = listen
        self.post_msg = post_msg
        self.proxy_open = proxy_open
        self.retry_login = retry_login
        self.retry_delay = retry_delay

    def initClient(self):

        retry_login = self.retry_login
        while retry_login > 0:
            if self._checkLoignStatus():
                return True

            if retry_login != self.retry_login:
                time.sleep(self.retry_delay)

            self._loginClient()

            retry_login -= 1

        return False

    def _checkLoignStatus(self):
        pass

    def _loginClient(self):
        pass



WEIBO_HEADERS = {
    'Host': "m.weibo.cn",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0",
    'Accept': "application/json, text/plain, */*",
    'Accept-Language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    'Accept-Encoding': "gzip, deflate, br",
    'Referer': "https://m.weibo.cn/",
    'X-Requested-With': "XMLHttpRequest",
    'MWeibo-Pwa': "1",
    'X-XSRF-TOKEN': "17399e",
    'Connection': "keep-alive",
    'Cookie': "WEIBOCN_FROM=1110006030; MLOGIN=1; _T_WM=27303904285; SUB=_2A25w1yBYDeRhGeFN6VQR9SvMyj-IHXVQOEAQrDV6PUJbkdANLVWtkW1NQESRl0W5CKpDvlfBo1zwxuRxr-casOEV; SUHB=0ftpBEk-jGDXMz; SCF=At_OdfrNW4n61fcPGR0Ky2hoen7fBjA6n8Yhq4GhmHCdBsyxbu38EpFAGNL8hdsMuxMHzLEuCmbnBHO-0KNm39s.; SSOLoginState=1574129673; XSRF-TOKEN=17399e; M_WEIBOCN_PARAMS=luicode%3D20000174%26uicode%3D20000174",
    'Pragma': "no-cache",
    'Cache-Control': "no-cache",
    'TE': "Trailers",

    }