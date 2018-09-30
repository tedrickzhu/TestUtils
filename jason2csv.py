import csv
import json
import sys

def trans(path):
    jsonData=open(path+'.json')
    #csvfile = open(path+'.csv', 'w')#此处这样写会导致写出来的文件会有空行
    #csvfile = open(path+'.csv', 'wb')#python2下
    csvfile = open(path+'.csv', 'w',newline='')#python3下
    for line in jsonData:#获取属性列表
        dic=json.loads(line[0:-2])
        keys=dic.keys()
        break
    writer = csv.writer(csvfile)
    writer.writerow(keys)#将属性列表写入csv中
    for dic in jsonData:#读取json数据的每一行，将values数据一次一行的写入csv中
        dic=json.loads(dic[0:-2])
        writer.writerow(dic.values())
    jsonData.close()
    csvfile.close()

if __name__ == '__main__':
    path=str(sys.argv[1])#获取path参数
    print (path)
    trans(path)