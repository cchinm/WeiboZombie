#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
'''

 * @version: 0.0.0
 * @Company: 
 * @Author: zhanming.zhang 
 * @Date: 2019/11/19 16:34 
 * @Last Modified by:   zhanming.zhang 
 * @Last Modified time: 2019/11/19 16:34
 * @Desc: 
'''

from WeiboBot.Bot import *
from WeiboBot.Bot.comment import CommentMixin
from WeiboBot.Bot.microblog import MicroblogMixin
from WeiboBot.Bot.info import UserInfoMixin

class WeiboZombie(MicroblogMixin,
                  CommentMixin,
                  UserInfoMixin):

    def __init__(self, zId):

        self.zId = zId
        self.Fetch = download.FetchRequest()
        self.headers = WEIBO_HEADERS.copy()


    def _getZombieRequestCookie(self, zombieId):

        cookieString = "SINAGLOBAL=8232569652899.277.1568279418551; ULV=1574041980247:9:1:1:8676145714081.492.1574041980244:1572500508523; SCF=AvMgkcJSk01oZ4y94F67qV38oC4Ctpc7JApVPtkvS4A4JUq9PYu8yIARTusO1XQm5qKobYge2_W1q2qIl3WiqY8.; SUHB=0M2FOs0Era_mNL; UOR=,,www.baidu.com; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFwU0JDDusDYA-AUfZ0mYLb5JpX5oz75NHD95QNe0zceh-feh20Ws4DqcjJi--Ni-2fiKL8i--fi-2fiKnNi--ci-zfi-zNi--RiKL8i-iWUG-t; SUB=_2A25w1yBbDeRhGeFN6VQR9SvMyj-IHXVQOEATrDV8PUJbkNBeLUHykW1NQESRl0mTMlCy6GVrnfyo5sriJ6A-QW7T; ALF=1576721675; wvr=6; _s_tentry=-; Apache=8676145714081.492.1574041980244; webim_unReadCount=%7B%22time%22%3A1574153862050%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D,MLOGIN=1; XSRF-TOKEN=deleted; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D231093_-_selffollowed%26oid%3D4435705494974740%26fid%3D1076035605732163%26uicode%3D10000011"
        return cookieString

    def _preGetSt(self):

        self.headers['Cookie'] = self._getZombieRequestCookie(self.zId)

        req = request.Request(method='GET',
                            url=checkLoginStatusAPI,
                            headers=self.headers,
                            # proxy=getRandomProxyHTTPS(),
                            timeout=5)
        resp = self.Fetch.fetch(req)
        json_resp = resp.json()['data']
        loginStatus = json_resp['login']

        print(json_resp)
        del req
        if loginStatus:
            return json_resp['st']
        else:
            # TODO: need login
            return


    def errCallback(self, json_resp):
        try:

            print(json_resp)
            if json_resp['ok'] == 1:
                return {"msg": "执行成功",
                        "code": 200,
                        "endTime": int(time.time())}
            elif json_resp['ok'] == -100:
                return {"msg": "登录失败",
                        "code": 403,
                        "endTime": int(time.time())}
            else:
                return {"msg": "执行失败",
                        "code": 500,
                        "error": json_resp['msg'],
                        "endTime": int(time.time())}
        except:
            return {"msg": "执行失败",
                    "code": 500,
                    "error": traceback.format_exc(),
                    "endTime": int(time.time())}


    def whichHeaders(self, **kwargs):
        headers = {
            'Host': "m.weibo.cn",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0",
            'Accept': "application/json, text/plain, */*",
            'Accept-Language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            'Accept-Encoding': "gzip, deflate, br",
            'X-Requested-With': "XMLHttpRequest",
            'MWeibo-Pwa': "1",
            'Content-Type': "application/x-www-form-urlencoded",
            'Content-Length': "99",
            'Origin': "https://m.weibo.cn",
            'Connection': "keep-alive",
            'Pragma': "no-cache",
            'Cache-Control': "no-cache",
            'TE': "Trailers",
            'Cookie': self._getZombieRequestCookie(self.zId),
            'cache-control': "no-cache"
        }
        headers.update(kwargs)
        return headers


if __name__ == '__main__':
    import pprint
    p = WeiboZombie(1)
    # t = p.onCreateComment(msg="微博zombie测试 切勿回复", oId="4407403644496546")
    # print(t)
    # print(p.cancelComment(oId="4407403644496546", cId="4440337198461926"))
    # print(p.cancelComment(oId="4407403644496546", cId="4440296676766005"))
    with open("C:\\Users\zhanming.zhang\Pictures\Saved Pictures\\index.jpg", "rb") as fp:
        fdata = fp.read()
    # t = p.updatePersonalInfo(
    #     uid="12",
    #     gender="m",
    #     province="15",
    #     city="0",
    #     year="1995",
    #     month="12",
    #     day="13",
    #     email="",
    #     url="",
    #     qq="",
    #     msn="",
    #     description="世界第一孤雕 立志成为最强的海贼王"
    # )
    t = p.queryPersonalInfo(uid="7326055013")
    pprint.pprint(t)