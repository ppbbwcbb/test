# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 19:21:46 2021

@author: 23716
"""

import requests
import json
from lxml import etree
from openpyxl import Workbook

url = "https://voice.baidu.com/act/newpneumonia/newpneumonia"
response = requests.get(url)

html = etree.HTML(response.text)
result = html.xpath('//*[@id="captain-config"]/text()')

result = json.loads(result[0])
result = result["component"][0]["caseList"]

wb = Workbook()
ws = wb.active
ws.title = "国内疫情"
ws.append(['地区','新增','现有','累计','治愈','死亡'])
for each in result:
    temp_list = [each['area'], each['confirmedRelative'], each['curConfirm'], 
                 each['confirmed'], each['crued'], each['died']]
    ws.append(temp_list)
    
wb.save("实时疫情报告.csv")