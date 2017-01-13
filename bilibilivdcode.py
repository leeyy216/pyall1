#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "$Author: wangxin.xie$"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2017-1-5 16:59$"

###############################################################
# 功能：模拟登录b站成功后,获取个人关注动态的视频信息
###############################################################
import urllib.request
import datetime
import sys
import http.cookiejar
import json
#####################全局变量###########################################

today = datetime.datetime.today()
todayStr = datetime.datetime.strftime(today, "%Y-%m-%d")
lastDayDate = today - datetime.timedelta(1)
lastDayDateStr = datetime.datetime.strftime(lastDayDate, "%Y-%m-%d")
picname="vdcode.png"
vdUrl="https://account.bilibili.com/captcha"
goLoginUrl="https://account.bilibili.com/login"
loginUrl="https://account.bilibili.com/login/dologin"
accountUrl="http://account.bilibili.cn/crossDomain?Expires=604800&DedeUserID=7385982&DedeUserID__ckMd5=258b1b7cb17d993c&SESSDATA=c4090d71,1450773446,55659e39&gourl=http://www.bilibili.com/"
mainUrl="http://www.bilibili.com/"
memberUrl="http://member.bilibili.com"
#################################################################

def getVdCode():
    '''获取验证码图片'''
    resp=urllib.request.urlopen(vdUrl)
    f = open(picname, 'wb')
    f.write(resp.read())
    f.close()
    print('VdCodePic Saved!')

def dealCookie():
    '''处理cookie'''
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)

def toLogin():
    '''进入登录页面'''
    resp = urllib2.urlopen(goLoginUrl)
    html = resp.read().decode('utf-8').encode('gbk')

def login():
    '''开始登录'''
    username=raw_input("please input your username: ")
    password=raw_input("please input your password: ")
    vdcode = raw_input("please input your vdcode: ")
    # 登录
    postDict = {
        'userid'      :username,
        'pwd'      : password,
        'vdcode'   : vdcode
    }
    postData = urllib.urlencode(postDict)
    req = urllib2.Request(loginUrl, postData)

    urllib2.urlopen(req)
    urllib2.urlopen(memberUrl)
    resp=urllib2.urlopen("http://member.bilibili.com/index.do?act=dynamic&page=1")

    #开始解析Python数据
    resp = resp.read().decode('utf-8').encode('gbk')
    data = json.loads(resp)
    print '------------------------------------------------'
    for i in range(10):
        print data[str(i)]['time_at']
        print data[str(i)]['uname']+': '+data[str(i)]['title']
        #因为播放数是数字,所以要转成字符串
        print '播放数: '.decode('utf-8')+str(data[str(i)]['play'])
        print '------------------------------------------------'

def main():
    print "===%s start===%s"%(sys.argv[0], datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S"))
    dealCookie()
    toLogin()
    getVdCode()
    login()
    print "===%s end===%s"%(sys.argv[0], datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S"))

#################################################################################
if __name__ == "__main__":
    main()
