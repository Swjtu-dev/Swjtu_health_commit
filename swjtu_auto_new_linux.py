#encoding: utf-8
import sys
import http.cookiejar
import urllib.parse
import codecs
import urllib.request
import time
import os
import re
from hashlib import md5
import subprocess
def str_clear(string):
    string=''.join(string)
    string=string.strip("\n")
    return string
dir=os.getcwd()
if not os.path.exists(dir+'//Data'):
    os.makedirs(dir+'//Data')
if not os.path.exists(dir+'//status'):
    os.makedirs(dir+'//status')
items = os.listdir(dir+'//Data')
datalist = []
for names in items:
  if names.endswith(".hel"):
    datalist.append(names)
for i in range(0,len(datalist)):
    #prepare
    file_now=str(datalist[i])
    file_name=file_now.split('.',1)
    file_name=file_name[0]
    if not os.path.exists(dir+'//status//status_health'+file_name+'.sta'):
        w=open(dir+'//status//status_health'+file_name+'.sta','w',encoding='utf-8')
        w.close
    now=time.strftime('%y%m%d')
    h = open(dir+'//Data//'+file_now,'r',encoding='utf-8')
    all = h.readlines()
    h.close()
    Uid=all[0:1]
    Pwd=all[1:2]
    IdCard=all[2:3]
    raw_post=all[3:4]
    Uid=str_clear(Uid)
    Pwd=str_clear(Pwd)
    IdCard=str_clear(IdCard)
    raw_post=str_clear(raw_post)
    UA='Mozilla/5.0 (iPhone; CPU iPhone OS 4_0_1 like Mac OS X) AppleWebKit/100.0.01 (KHTML, like Gecko) Version/0.0.1 Mobile/100000 Safari/100.0'
    Pwd=urllib.parse.quote(Pwd)
    print(Pwd)
    url = "http://xgsys.swjtu.edu.cn/SPCPTest/Web/Account/IdCardLogin"
    raw_po='txtUid='+str(Uid)+'&txtPwd='+str(Pwd)+'&txtIdCard='+str(IdCard)+'&codeInput='
    print(raw_po)
    header = {
        'Content-Length':'80',
        'Cache-Control':'max-age=0',
        'Origin': 'http://xgsys.swjtu.edu.cn',
        'Upgrade-Insecure-Requests': '1',
        'DNT': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': UA,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://xgsys.swjtu.edu.cn/spcptest/web/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive'
     }
    raw_po_e=raw_po.encode('utf-8')
    req=urllib.request.Request(url=url,headers=header,data=raw_po_e)
    cj = http.cookiejar.CookieJar()
    opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    r = opener.open(req)
    cookieStr = ''
    for item in cj:
        cookieStr = cookieStr + item.name + '=' + item.value + ';'
    print(cookieStr)
    url_request="http://xgsys.swjtu.edu.cn/SPCPTest/Web/Report/Index"
    header_selfdefine={
        'Host': 'xgsys.swjtu.edu.cn',
        'Content-Length': '2097',
        'Cache-Control': 'max-age=0',
        'Origin': 'http://xgsys.swjtu.edu.cn',
        'Upgrade-Insecure-Requests': '1',
        'DNT': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': UA,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://xgsys.swjtu.edu.cn/SPCPTest/Web/Report/Index',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': cookieStr,
        'Connection': 'keep-alive'
    }
    f = open(dir+'//status//status_health'+file_name+'.sta','r',encoding='utf-8')
    data = f.readlines()
    f.close()
    now=list(now)
    now.insert(2,'-')
    now.insert(5,'-')
    now=''.join(now)
    date='20'+str(now)
    print(date)
    if not(date in data):
        for t in range (0,100):
            print("request")
            print(raw_post)
            raw_e=raw_post.encode('utf-8')
            request_obj=urllib.request.Request(url=url_request,headers=header_selfdefine,data=raw_e)
            response_obj=urllib.request.urlopen(request_obj)
            status=response_obj.status
            print(response_obj.status)
            if str(status)=='200':
                w=open(dir+'//status//status_health'+file_name+'.sta','w',encoding='utf-8')
                w.write(date)
                w.close
                print("OK")
                break
            else:
                time.sleep(10)
        else:
            print('error')
            time.sleep(10)
