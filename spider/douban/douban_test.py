#encoding=utf-8
import requests
from lxml import etree

url = 'https://movie.douban.com/subject/1292052'
data = requests.get(url).text
s=etree.HTML(data)

'''
通过分析网页html的源码，将对应元素的xpath拷贝过来，获得元素的对应的值
'''
#type = list
filmname = s.xpath('//*[@id="content"]/h1/span[1]/text()')
director = s.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')
# //*[@id="info"]/span[1]/span[2]
#不同的主演区别在于a[n]
actor1 = s.xpath('//*[@id="info"]/span[3]/span[2]/a[1]/text()')
actor2 = s.xpath('//*[@id="info"]/span[3]/span[2]/a[2]/text()')
# //*[@id="info"]/span[3]/span[2]
#获得所有的主演,使用a
actors = s.xpath('//*[@id="info"]/span[3]/span[2]/a/text()')

time = s.xpath('//*[@id="content"]/span[13]/text()')


#type = lxml.etree._ElementUnicodeResult
filmname = filmname[0]
#转码
filmname.encode('utf-8')

print(filmname)
print('director:',director)


#http://t.cn/RYwhs5H