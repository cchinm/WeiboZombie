#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
'''

 * @version: 0.0.0
 * @Company: 
 * @Author: zhanming.zhang 
 * @Date: 2019/11/19 17:00 
 * @Last Modified by:   zhanming.zhang 
 * @Last Modified time: 2019/11/19 17:00
 * @Desc: 
'''

import base64
import time
import requests







if __name__ == '__main__':
    import os
    dirpath = "C:\\Users\zhanming.zhang\Pictures\Saved Pictures\\index1.jpg"
    fp = open(dirpath, "rb")
    img = fp.read()
    fp.close()
    print(base64.b64encode(img))
    d = int(time.time() * 1000)
    uri = "https://account.weibo.com/set/aj5/photo/uploadv6?cb=https%3A%2F%2Fweibo.com%2Faj%2Fstatic%2Fupimgback.html" \
          "%3F_wv%3D5%26callback%3DSTK_ijax_{}".format(d)
    filedata = base64.b64encode(img)
    payload = {"Filedata": filedata,
               "ax": "79.33333333333334",
               "ay": "10.833333333333323",
               "aw": "198.33333333333334",
               "type": "jpeg",
               "file_source": "5"}


    print(len(img), len(filedata), os.path.getsize(dirpath))
    payload = {"Filedata":filedata,
               "ax":"79.33333333333334",
               "ay":"10.833333333333323",
               "aw":"198.33333333333334",
               "type":"jpeg",
               "file_source":"5"}
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
        'Referer': "https://weibo.com/7326055013/profile?topnav=1&wvr=6&is_all=1",
        'Cookie': "SINAGLOBAL=8232569652899.277.1568279418551; ULV=1574041980247:9:1:1:8676145714081.492.1574041980244:1572500508523; SCF=AvMgkcJSk01oZ4y94F67qV38oC4Ctpc7JApVPtkvS4A4JUq9PYu8yIARTusO1XQm5qKobYge2_W1q2qIl3WiqY8.; SUHB=0M2FOs0Era_mNL; UOR=,,www.baidu.com; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFwU0JDDusDYA-AUfZ0mYLb5JpX5oz75NHD95QNe0zceh-feh20Ws4DqcjJi--Ni-2fiKL8i--fi-2fiKnNi--ci-zfi-zNi--RiKL8i-iWUG-t; SUB=_2A25w1yBbDeRhGeFN6VQR9SvMyj-IHXVQOEATrDV8PUJbkNBeLUHykW1NQESRl0mTMlCy6GVrnfyo5sriJ6A-QW7T; ALF=1576721675; wvr=6; _s_tentry=-; Apache=8676145714081.492.1574041980244; webim_unReadCount=%7B%22time%22%3A1574153862050%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D,MLOGIN=1; XSRF-TOKEN=deleted; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D231093_-_selffollowed%26oid%3D4435705494974740%26fid%3D1076035605732163%26uicode%3D10000011",
        'Upgrade-Insecure-Requests': "1",
        'Pragma': "no-cache",
        'Cache-Control': "no-cache",
        'Postman-Token': "f42df093-3d88-491c-826f-46f60b79fe88,ece032b1-5512-456e-84f0-af9432d0bddf",
        'cache-control': "no-cache"
    }
    print(uri)
    req = requests.request('POST', url=uri, data=payload, headers=headers)
    # print(req)
    print(req.url)
    req.raise_for_status()