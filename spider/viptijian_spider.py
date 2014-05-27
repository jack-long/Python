# -*- coding: utf-8 -*-

#  introduction
#  针对 中康体检网http://www.viptijian.com 的网页爬虫
#  取得站点所提供的全国体检中心基本信息
#  
# The result data.txt may look like this:
#
# city:北京
# 中国人民解放军第309医院体检中心
# 公立医院： 公立三甲
# 所在区域：北京市 海淀区
# 医院地址：北京市海淀区黑山扈路甲17号 
# 
# 中国人民解放军海军总医院体检中心
# 公立医院： 公立三甲
# 所在区域：北京市 海淀区
# 医院地址：北京市海淀区阜成路6号 
# ...
# city:重庆
# 爱康国宾重庆黄泥磅揽胜国际体检分院
# 公立医院： 民营品牌
# 所在区域：重庆市 渝北区
# 医院地址：重庆市渝北区长安丽都揽胜国际广场2层（长都假日酒店对面） 
#
# 声明：本程序仅供学习、交流Python技术目的，严禁恶意、非法使用。

import urllib2
import re

source = 'http://www.viptijian.com/0351/UnitsList-0401.html'
base = "http://www.viptijian.com"
database = ''

# Windows Path to Desktop
WinPath = "C:\Users\Public\Desktop\\" 
# Linux Path, the result will be besides the file "spider.py"
LinuxPath = ''

# You May Change This !!!
filepath = LinuxPath
filename = "data.txt"

html = urllib2.urlopen(source).read()
print "open source page success"
patten = r'class="js-hotcitylist" href="(.+?)" class="js-hotcitylist">\s+(.+?)</a>'
cityinfo = re.findall(patten, html)

for url, city in cityinfo:
    database += 'city:'+city+'\n'
    print "City", city
    html = urllib2.urlopen(base+url).read()
    patten = r'-0-0-0-0-0-(\w+).html'
    match = re.findall(patten, html)
    patten = r'class="fl"> (.+?)</a>.+?<li>(.+?)</li>\s+<li>(.+?)</li>\s+<li>(.+?)<a'
    if not match:
        units = re.findall(patten, html, re.DOTALL)
        if not units:
            print "No Units in this city yet.\n\n"
            database += "No Units in this city yet.\n\n"
            continue
        for Name, Class, Region, Address in units:
            database += Name+'\n'+Class+'\n'+Region+'\n'+Address+'\n\n'
        continue
    
    total = int(match[-1])
    index = 1
    while index <= total:
        page =  base+url[:-5]+'-0-0-0-0-0-'+str(index)+'.html'
        print "reading page", page
        html = urllib2.urlopen(page).read()
        units = re.findall(patten, html, re.DOTALL)
        for Name, Class, Region, Address in units:
            database += Name+'\n'+Class+'\n'+Region+'\n'+Address+'\n\n'
        index += 1
print "data processing finished!"

f = open(filepath+filename, 'w')
f.write(database)
f.close()
print "Bye!"