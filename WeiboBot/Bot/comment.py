#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
'''

 * @version: 0.0.0
 * @Company: 
 * @Author: zhanming.zhang 
 * @Date: 2019/11/19 16:29 
 * @Last Modified by:   zhanming.zhang 
 * @Last Modified time: 2019/11/19 16:29
 * @Desc: 评论操作类
'''

from WeiboBot.Bot import *

class CommentMixin:


    @weiboBottle
    def onCreateComment(self, msg, oId):
        """

        :param msg: 评论内容
        :param oId: 评论ID
        :return:
        """

        St = self._preGetSt()
        if St is None:
            # TODO: need login and Put it back in Queue again.
            return
        print(St)

        payload = {"content": msg,
                   "mid": oId,
                   "st": St,
                   "_spr": "screen:1920x1080"}
        headers = self.whichHeaders()
        headers['X-XSRF-TOKEN'] = St
        headers['Referer'] = "https://m.weibo.cn/detail/%s" % oId

        req = request.Request(
            method='POST',
            url=createCommentAPI,
            data=payload,
            headers=headers)
        resp = self.Fetch.fetch2(method=req.method,
                                 url=req.url,
                                 headers=req.headers,
                                 data=req.data)
        json_resp = resp.json()
        return self.errCallback(json_resp)

    @weiboBottle
    def onLikeComment(self, oId, cId):
        """

        :param oId:
        :param cId:
        :return:
        """

        St = self._preGetSt()
        if St is None:
            # TODO:....
            return

        payload = {"id": cId,
                   "type": "comment",
                   "st": St,
                   "_spr": "screen:1920x1080"}
        headers = self.whichHeaders()
        headers['X-XSRF-TOKEN'] = St
        headers['Referer'] = "https://m.weibo.cn/detail/%s" % oId

        req = request.Request(
            method='POST',
            url=postLikeCommentAPI,
            data=payload,
            headers=headers)
        resp = self.Fetch.fetch2(method=req.method,
                                 url=req.url,
                                 headers=req.headers,
                                 data=req.data)
        json_resp = resp.json()
        return self.errCallback(json_resp)


    onLikeReplyComment = onLikeComment  # 点赞评论


    @weiboBottle
    def cancelComment(self, oId, cId):

        St = self._preGetSt()
        if St is None:
            return

        payload = {"st": St,
                   "cid": cId,
                   "_spr": "screen:1920x1080",
                   }
        headers = self.whichHeaders()
        headers['X-XSRF-TOKEN'] = St
        headers['Referer'] = "https://m.weibo.cn/detail/%s" % oId

        req = request.FormRequest(
            url=destoryCommentAPI,
            data=payload,
            headers=headers
        )
        resp = self.Fetch.fetch2(method=req.method,
                                 url=req.url,
                                 data=req.data,
                                 headers=req.headers)
        json_resp = resp.json()
        return self.errCallback(json_resp)

    @weiboBottle
    def cancelLike(self, oId, cId):
        """

        :param oId: 如果取消评论点赞cId必须不为None；仅仅取消微博点赞则cId必须为None
        :param cId:
        :return:
        """

        St = self._preGetSt()
        print("St", St)
        if St is None:
            # TODO:..
            return

        headers = self.whichHeaders()
        headers['X-XSRF-TOKEN'] = St
        headers['Referer'] = "https://m.weibo.cn/detail/%s" % oId
        if cId is None:
            # 仅仅取消微博点赞
            payload = {"id": oId,
                       "attitude": "heart",
                       "st": St,
                       "_spr": "screen:1920x1080"}
            req = request.FormRequest(
                url=destoryLikeMicroblogAPI,
                data=payload,
                headers=headers
            )
        else:
            payload = {"id": cId,
                       "type": "comment",
                       "st": St,
                       "_spr": "screen:1920x1080"}
            req = request.FormRequest(
                url=destoryLikeCommentAPI,
                data=payload,
                headers=headers
            )

        resp = self.Fetch.fetch2(method=req.method,
                                 url=req.url,
                                 data=req.data,
                                 headers=req.headers)
        json_resp = resp.json()
        return self.errCallback(json_resp)

    @weiboBottle
    def cancelLikeComment(self, oId, cId):
        return self.cancelLike(oId, cId)




