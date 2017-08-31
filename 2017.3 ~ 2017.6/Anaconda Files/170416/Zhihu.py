# -*- coding: utf-8 -*-



import urllib2
import re
import requests
import HTMLParser
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
url = "http://daily.zhihu.com/"

## 获取源码
def getHtml(url):
    header = {'User-Agent' :'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER'}
    request = urllib2.Request(url,headers = header)
    response = urllib2.urlopen(request)
    text = response.read()
#    print text
    return text

html = getHtml(url)
## 获取网址 超链接
urls = []
def getUrls(html):
    pattern = re.compile('<a href="/story/(.*?)"')
    items = re.findall(pattern,html)
#    print items
    for item in items:
        urls.append('http://daily.zhihu.com/story/' + item)
#        print urls[-1]
    return urls

urls = getUrls(html)

## 标题 正文 
def getContent(url):
    html = getHtml(url)
    pattern = re.compile('<h1 class="headline-title">(.*?)</h1>')
    items = re.findall(pattern,html)
    print items[0] ## 标题
    
    pattern = re.compile('<div class="content">\\n<p>(.*?)</div>',re.S) ## re.S 多行匹配
    items_withtag = re.findall(pattern,html)
#    print items_withtag
    for item in items_withtag:
        print item



for url in urls:    
    try:
        getContent(url)
    except Exception,e:
        print e














    
