#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
'''

 * @version: 0.0.0
 * @Company: 
 * @Author: zhanming.zhang 
 * @Date: 2019/11/16 15:53 
 * @Last Modified by:   zhanming.zhang 
 * @Last Modified time: 2019/11/16 15:53
 * @Desc: 
'''

import requests
from WeiboBot.RepackHttp.Http import (
                  logging,
                  traceback)
from WeiboBot.RepackHttp.Http.response import Response


class FetchRequest:



    def fetch(self, request):
        logging.debug("%s %s" % (request, request.url))
        try:
            proxies = request.meta.get('proxy', None)
            print(request.headers,)

            _resp = requests.request(method=request.method.upper(),
                                     url=request.url,
                                     headers=request.headers,
                                     # proxies=proxies
                                     )
            print(_resp)
            resp = Response(url=_resp.url,
                            request=request,
                            response=_resp,
                            headers=_resp.headers,
                            **request.meta)
            if request.callback:
                return request.callback(resp)
            return resp
        except:
            traceback.print_stack()
            logging.error("Fetch Error %s %s" % (request, request.url))
            logging.debug("Error Reason: "+traceback.format_exc() )


    def fetch2(self, method, url, headers, data=None):

        resp = requests.request(method=method.upper(),
                                url=url,
                                headers=headers,
                                data=data)
        return resp