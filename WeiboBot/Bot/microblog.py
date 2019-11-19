#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
'''

 * @version: 0.0.0
 * @Company: 
 * @Author: zhanming.zhang 
 * @Date: 2019/11/19 16:29 
 * @Last Modified by:   zhanming.zhang 
 * @Last Modified time: 2019/11/19 16:29
 * @Desc: 
'''


from WeiboBot.Bot import *

class MicroblogMixin:

    @weiboBottle
    def onLikeMicroblog(self, oId):
        """

        :param oId:
        :return:
        """
        St = self._preGetSt()
        if St is None:
            # 　todo:something
            return
        payload = {"id": oId,
                   "attitude": "heart",
                   "st": St,
                   "_spr": "screen:1920x1080"}
        headers = self.whichHeaders()
        headers['X-XSRF-TOKEN'] = St
        headers['Referer'] = "https://m.weibo.cn/detail/%s" % oId

        req = request.Request(
            method='POST',
            url=postLikeMicroblogAPI,
            data=payload,
            headers=headers)
        resp = self.Fetch.fetch2(method=req.method,
                                 url=req.url,
                                 headers=req.headers,
                                 data=req.data)
        json_resp = resp.json()
        return self.errCallback(json_resp)


    @weiboBottle
    def cancelLikeMicroblog(self, oId):
        return self.cancelLike(oId, None)