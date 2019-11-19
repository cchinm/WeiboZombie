#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
'''

 * @version: 0.0.0
 * @Company: 
 * @Author: zhanming.zhang 
 * @Date: 2019/11/16 15:28 
 * @Last Modified by:   zhanming.zhang 
 * @Last Modified time: 2019/11/16 15:28
 * @Desc: 对请求对象进行包装
'''


class Request:


    def __init__(self,
                 method,
                 url,
                 headers,
                 data=None,
                 callback=None,
                 json=None,
                 **meta):
        self.method = method.upper()
        self.url = url
        self.headers = headers
        self.data = data or json
        self.meta = meta or dict()
        self.callback = callback


    def __str__(self):

        return "<%s %s>" % (self.method, hex(id(self)))



class FormRequest(Request):


    def __init__(self, url, headers, data, callback=None, **meta):
        super(FormRequest, self).__init__(method='POST',
                                          url=url,
                                          headers=headers,
                                          data=data,
                                          callback=callback,
                                          **meta)

