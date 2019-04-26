import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlopen
import os, time, sys
import re
import chardet
from boilerpipe.extract import Extractor
def get_text(url):
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.string
    #获得标题title
    extractor = Extractor(extractor='ArticleExtractor', url=url)
    title = title.strip()
    title = title.encode('gbk','ignore')
    content = extractor.getText().encode('gbk','ignore')
    file = open('D:/details.txt', 'wb+')
    file.write(title)
    file.write(content)

get_text('https://mp.weixin.qq.com/s/wNmK6L7nEWRSJKHWiDUrtQ')
# if __name__ == "__main__":
#     url = 'https://mp.weixin.qq.com/s/wNmK6L7nEWRSJKHWiDUrtQ'
#     #url = 'https://mp.weixin.qq.com/s/KWQ7CqfFJLSREROvqEVQtA'
#     get_text(url)
#     sys.exit()
