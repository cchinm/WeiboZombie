#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
'''

 * @version: 0.0.0
 * @Company: 
 * @Author: zhanming.zhang 
 * @Date: 2019/11/16 15:20 
 * @Last Modified by:   zhanming.zhang 
 * @Last Modified time: 2019/11/16 15:20
 * @Desc: 返回的response对象进行包装
'''

from WeiboBot.RepackHttp.Http import *

class Response:


    def __init__(self,
                 url,
                 request,
                 headers,
                 response,
                 **meta):

        self.url = url
        self.__request = request
        self.headers = headers
        self.meta = meta
        self.__response = response


    @property
    def text(self):
        return self.__response.text

    @property
    def content(self):
        return self.__response.content

    @property
    def status(self):
        """
        返回状态吗
        :return:
        """
        return self.__response.status_code

    def resp(self):
        """
        返回响应对象
        :return:
        """
        return self.__response

    def req(self):
        """
        返回请求对象
        :return:
        """
        return self.__request

    def json(self):
        """
        json反序列化
        :return:
        """
        return self.__response.json()


    def html(self, encoding="utf8"):
        """
        html标签解析
        :return:
        """
        if encoding is None:
            encode = chardet.detect(self.content)
            encoding = encode['encoding']

        return lxml.html.fromstring(self.content.decode(encoding, "ignore"))

