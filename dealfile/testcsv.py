# import csv
# import pandas as pd
#
path = "../ML4203/train.csv"
# a = open(path, "r")
# Hlength=len(a.readlines())
# data_x= pd.read_csv(filepath_or_buffer = path, sep = ',')["lo"].values
# data_y= pd.read_csv(filepath_or_buffer = path, sep = ',')["la"].values
# f=open('jingweidu2.text', 'w')
# for i in range(0,Hlength):
#     print(data_x[i],data_y[i])
#     f.write(str(data_x[i]))
#     f.write(' ')
#     f.write(str(data_y[i]))
#     f.write('\n')
# f.close()

# import csv
#
# with open('../ML4203/train.csv', 'U') as csvfile:
#     reader = csv.DictReader(csvfile)
#     # print(str(reader))
#     dataset = []
#     count = 0
#     keys = reader.fieldnames
#     # print(keys)
#     for key_i in range(3,len(keys)):
#         key = keys[key_i]
#         # print(key[-1])
#         column = []
#         for row in reader:
#             column.append(row[key])
#
#         column.append(key[-1])
#         dataset.append(column)
#     # print(len(dataset))
# print(dataset)


# import csv
# with open('/Users/wangzhao/Downloads/test.csv', 'U') as csvfile:
#     reader = csv.reader(csvfile)
#     column = [row[2] for row in reader]
# print(column)


# 1.基本的读取文件的方式
#
# import csv
# csv_reader=csv.reader(open('taxi.csv',encoding='utf-8'))
# for row in csv_reader:
#     print(row)
# #taxi.csv最好放在同一目录下
#
# 2.读取文件中的某一列以及多列
#
# import csv
# with open('taxi1.csv',encoding='utf-8') as csvfile:
#     reader=csv.reader(csvfile)
#     column=[row[2] for row in reader]
#     print(column)
#
#
# ####方法2
# data_x= pd.read_csv(filepath_or_buffer = 'taxi1.csv', sep = ',')["lo"].values
# data_y= pd.read_csv(filepath_or_buffer = 'taxi1.csv', sep = ',')["la"].values
#
# 3.读取文件的某一行
#
import csv
with open(path,encoding='utf-8') as csvfile:
    reader=csv.reader(csvfile)
    dataset = []
    for i,rows in enumerate(reader):
        if i==0:
            row=rows
    print(type(row))
    print(row)
# ###
# ['id', 'dest_no', 'lo', 'la', 'gps_time', 'status', 'speed', 'vehicle_type', 'taxi_no_color', 'dir', 'create_time']
#
# 4.读取文件的行数
#
# import csv
# a=open("taxi1.csv","r")
# b=len(a.readline())
# print(b)



