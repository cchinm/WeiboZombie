#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
'''

 * @version: 0.0.0
 * @Company: 
 * @Author: zhanming.zhang 
 * @Date: 2019/11/16 15:18 
 * @Last Modified by:   zhanming.zhang 
 * @Last Modified time: 2019/11/16 15:18
 * @Desc: 再打包request请求，方便内部企业开发。共有一套请求方式
'''

import ssl
import urllib.parse
import requests
import lxml.html
import traceback
import chardet
from WeiboBot.RepackHttp.util.logging import logging

