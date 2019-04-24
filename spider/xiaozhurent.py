#encoding=utf-8

import requests
from lxml import etree

for a in range(1,6):
    url = 'http://cd.xiaozhu.com/search-duanzufang-p{}-0/'.format(a)
    data = requests.get(url).text

    s = etree.HTML(data)
    file = s.xpath('//*[@id="page_list"]/ul/li')

    for div in file:
        title = div.xpath('./div[2]/div/a/span/text()')[0].encode('utf-8')
        price = div.xpath('./div[2]/span[1]/i/text()')[0].encode('utf-8')
        scrible = div.xpath('./div[2]/div/em/text()')[0].encode('utf-8').strip()
        pic = div.xpath('./a/img/@lazy_src')[0]
        print('{},{},{},{}'.format(title,price,scrible,pic))