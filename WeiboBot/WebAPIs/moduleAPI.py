#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
'''

 * @version: 0.0.0
 * @Company: 
 * @Author: zhanming.zhang 
 * @Date: 2019/11/19 9:42 
 * @Last Modified by:   zhanming.zhang 
 * @Last Modified time: 2019/11/19 9:42
 * @Desc: 模块API， 包括发微博，转发，评论，点赞
'''


postLikeMicroblogAPI = "https://m.weibo.cn/api/attitudes/create"
# {"表单数据":{"id":"4398442228910565","attitude":"heart","st":"75371a","_spr":"screen:1920x1080"}}


postLikeCommentAPI = "https://m.weibo.cn/api/likes/update"
# {"表单数据":{"id":"4440363307556049","type":"comment","st":"75371a","_spr":"screen:1920x1080"}}

createCommentAPI = "https://m.weibo.cn/api/comments/create"
# { "content":"好棒棒喔",
#   "mid":"4407403644496546",
#   "st":"a4dbc8",
#   "_spr":"screen:1920x1080"}

replyCommentAPI = "https://m.weibo.cn/api/comments/reply"
# {"id":"4398442228910565",
# "reply":"4440297213355422",
#  "content":"干嘛喔 自己评论自己都不行哈",
#  "withReply":"1",
#  "mid":"4398442228910565",
#  "cid":"4440297213355422",
#  "st":"27e081",
#  "_spr":"screen:1920x1080"}}


destoryCommentAPI = "https://m.weibo.cn/comments/destroy"
# {"cid":"4440348434495108","st":"eaf3a5","_spr":"screen:1920x1080"}
destoryLikeCommentAPI = "https://m.weibo.cn/api/likes/destroy"
# {"表单数据":{"id":"4440363361657666","type":"comment","st":"134f7d","_spr":"screen:1920x1080"}}
destoryLikeMicroblogAPI = "https://m.weibo.cn/api/attitudes/destroy"
# {"表单数据":{"id":"4398442228910565","attitude":"heart","st":"3f350a","_spr":"screen:1920x1080"}}



saveUserInfoAPI = "https://m.weibo.cn/settingDeal/inforSave"
# {"表单数据":{"gender":"f","province":"15","city":"0",
# "year":"1995","month":"12","day":"13","email":"xwz@yatsenglobal.com",
# "url":"http://www.perfectdiary.com/","qq":"119162","msn":"",
# "description":"闲云野鹤 过路一只"}}

# {"表单数据":{"st":"f9bc5c","screen_name":"神奇海螺完美日记"}}


queryUserInfoURI = "https://m.weibo.cn/users/{uid}?set=1"
# html

iconUploadAPI = "https://account.weibo.com/set/aj5/photo/uploadv6?cb=https%3A%2F%2Fweibo.com%2Faj%2Fstatic%2Fupimgback.html%3F_wv%3D5%26callback%3DSTK_ijax_{}"
# GET：{"cb":""https://weibo.com/aj/static/upimgback.html?_wv=5&callback=STK_ijax_157415376705436""}
# POST:{"Filedata":"",
# "ax":"79.33333333333334",
# "ay":"10.833333333333323",
# "aw":"198.33333333333334",
# "type":"jpeg",
# "file_source":"5"}}

