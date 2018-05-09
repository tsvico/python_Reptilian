#encoding: utf-8
import requests
from bs4 import BeautifulSoup
PAGE_URL_LIST = []
BESE_PAGE_URL = "https://www.doutula.com/photo/list/?page="
for x in range(1,1500):
    url = BESE_PAGE_URL + str(x)
    PAGE_URL_LIST.append(url)


for page_url in PAGE_URL_LIST:
    #url请求
    response = requests.get(page_url)
    #使用返回的数据构建ｂｅｓｕ对象

    #requests对象中　response.content返回的是二进制的数值，
    # response.text返回的是Unicode型的数据
    # 也就是说，如果你想获取文本，可以通过.text
    # 如果你想获取图片，文件可以通过　.content
    soup = BeautifulSoup(response.content,'lxml')
