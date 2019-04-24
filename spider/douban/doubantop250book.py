#encoding=utf-8

import requests

from lxml import etree

#通过分析url的规律知道，每个url的差异在于结尾处的数字不同，
# 所以可以构造出多个url然后爬取数据
for a in range(10):
    url = 'https://book.douban.com/top250?start={}'.format(a*25)
    data = requests.get(url).text

    s = etree.HTML(data)
    file = s.xpath('//*[@id="content"]/div/div[1]/div/table')

    for div in file:
        title = div.xpath('./tr/td[2]/div[1]/a/@title')[0].encode('utf-8')
        href = div.xpath('./tr/td[2]/div[1]/a/@href')[0].encode('utf-8')
        score = div.xpath('./tr/td[2]/div[2]/span[2]/text()')[0].encode('utf-8')
        num = div.xpath('./tr/td[2]/div[2]/span[3]/text()')[0].encode('utf-8').strip('(').strip().strip(')')
        scible = div.xpath('./tr/td[2]/p[2]/span/text()')
        # print(scible)
        if len(scible)>0:
            scible = scible[0].encode('utf-8')
            print('{} {} {} {} {}'.format(title,href,score,num,scible))
        else:
            print('{} {} {} {}'.format(title, href, score, num))

