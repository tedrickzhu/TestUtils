#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:spider.py
#time:2019/1/7 下午3:19

import requests as req
from bs4 import BeautifulSoup

def main():
    ajax_url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
    headers = {
        'Referer':'https://www.lagou.com/jobs/list_Python?labelWords=&fromSearch=true&suginput=',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'X-Anit-Forge-Code':'0',
        'X-Anit-Forge-Token': None,
        'X-Requested-With': 'XMLHttpRequest'
    }
    form_data = {
        'first':'true',
        'pn':'1',
        'kd':'Python'
    }

    result = req.post(ajax_url,headers=headers,data=form_data)
    print(result.content)
    pass

if __name__ == '__main__':

    main()
    pass