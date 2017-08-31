# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 20:54:17 2017

@author: Administrator
"""

import requests
import re

html = requests.get('http://www.haoip.cc/tiqu.htm')

ip_content = re.findall(r'r/>(.*?)<b',html.text,re.S)

for i in ip_content:
    i = re.sub('\n','',ip)
    print i