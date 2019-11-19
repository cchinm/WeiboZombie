#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
'''

 * @version: 0.0.0
 * @Company: 
 * @Author: zhanming.zhang 
 * @Date: 2019/11/19 16:21 
 * @Last Modified by:   zhanming.zhang 
 * @Last Modified time: 2019/11/19 16:21
 * @Desc: 
'''

from WeiboBot.Utils import *

def weiboBottle(func):
    """
    负责将返回信息返回
    :param func:
    :return:
    """

    def innerWrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            if res is None:
                #TODO:是否需要重新登录进行再次请求还是直接放弃?
                return {"msg":"登录失败",
                        "code":403,
                        "endTime":int(time.time())}
            else:
                return res
        except :
            print("fail")
            return {"msg": "执行失败",
                    "code": 500,
                    "error": traceback.format_exc(),
                    "endTime": int(time.time())}
    return innerWrapper