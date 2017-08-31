# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 13:43:48 2017

@author: Administrator
"""

import urllib2
import re
import requests
import HTMLParser
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
url = "http://daily.zhihu.com/"

def getHtml(url):
    header = {'User-Agent' :'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER'}
    request = urllib2.Request(url,headers = header)
    response = urllib2.urlopen(request)
    text = response.read()
    print text
    return text

html = getHtml(url)
