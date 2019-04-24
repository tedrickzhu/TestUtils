#encoding=utf-8

from lxml import etree
import requests

'''
对于动态加载的页面，首先需要分析下网站，使用浏览器，分析XHR部分的内容发现
每点击一次'加载更多'，页面给予XHR部分返回了一个json文件，其内容即为新加载出来的内容，
分析每次加载出来的页面的URL的异同点，寻找规律
'''

for a in range(3):
    url = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start={}'.format(a*20)
    file = requests.get(url).json()
    for i in range(20):
        dict = file['data'][i] #循环取出第i部电影的信息
        urlname = dict['url']
        title = dict['title'].encode('utf-8')
        rate = dict['rate'].encode('utf-8')
        cast = dict['casts']

        print('{},{},{},{}'.format(title,rate,' '.join(cast).encode('utf-8'),urlname))