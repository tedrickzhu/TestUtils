import os

path = 'I:/awfulmess/pppp/v1_0/'

file_list = os.listdir(path)
for file in file_list:
    name =file.split('.')
    # print(name)
    if len(name) >1:
        if name[1]!='com':
            newname = str(name[0])+'.mp4'
            os.rename(path+file,path+newname)
        if name[1]=='com':
            newname = str(name[0])+'.com.mp4'
            os.rename(path+file,path+newname)