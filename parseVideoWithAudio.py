#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:parseVideoWithAudio.py
#time:2019/7/31 下午3:54

import os
os.environ["FFMPEG_BINARY"] = "/usr/local/bin/ffmpeg"

from os import listdir
from moviepy.editor import *
import cv2 as cv

'''
use moviepy combine video and audio ,mac default player canot play with audio,please change another player
use ffmpeg get audio from video
ffmpeg -i test.mp4 -f mp3 test2.mp3
use ffmpeg combine video and audio
ffmpeg -i testnoau.mp4 -i test.mp3 -strict -2 -f mp4 testau5.mp4

1，使用OpenCV读取source视频，将每一帧的特定区域取出，生成新的无音视频写入硬盘
2，使用moviepy读取source视频，提取出音频，读入无音视频，添加声音，生成最终视频，写入硬盘
3,moviepy将读入的视频再写入原视频时会出错，文件会被破坏，需要写入新的文件

使用多个工具的最大的问题是格式没法统一。将硬盘作为中介，反复与硬盘交互
'''

def editVideo(videofile,cvdesvideo,desvideo,destime,deslocat):
    print("cut video start:------"+videofile+"\n")
    capture = cv.VideoCapture(videofile);
    nbFrames = int(capture.get(cv.CAP_PROP_FRAME_COUNT))
    width = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))
    fps = capture.get(cv.CAP_PROP_FPS)
    # codec = capture.get(cv.CAP_PROP_FOURCC)
    # codec = cv.VideoWriter_fourcc(*'XVID')
    codec = cv.VideoWriter_fourcc(*"mp4v")
    # codec = cv.VideoWriter_fourcc(*"MP42")
    # codec = cv.VideoWriter_fourcc('P','I','M','1')
    # codec = cv.VideoWriter_fourcc('M', 'P', '4', '2')
    # codec = cv.VideoWriter_fourcc('D', 'I', 'V', '3')
    # codec = cv.VideoWriter_fourcc('D', 'I', 'V', 'X')
    # codec = cv.VideoWriter_fourcc('F', 'L', 'V', '1')
    # codec = cv.VideoWriter_fourcc('M','J','P','G')
    deswidth =width if deslocat[1]==-1 else deslocat[1]-deslocat[0]
    desheight =height if deslocat[3]==-1 else deslocat[3]-deslocat[2]
    deswidth = deswidth if deswidth<=width else width - deslocat[0]
    desheight = desheight if desheight<=height else height - deslocat[2]
    # outvideo = cv.VideoWriter(cvdesvideo, codec, fps, (width,height))
    outvideo = cv.VideoWriter(cvdesvideo, codec, fps, (deswidth,desheight))

    startframenum =int(nbFrames if fps*destime[0]>nbFrames else fps*destime[0])
    endframenum =int(nbFrames if fps*destime[1]>nbFrames else fps*destime[1])
    if startframenum == endframenum:
        return -1
    if startframenum > endframenum:
        tempnum = startframenum
        startframenum = endframenum
        endframenum = tempnum
    for f in xrange(0,startframenum):
        _,_ = capture.read()
    for k in xrange(startframenum,endframenum):
        ret, frameImg = capture.read()
        # print(frameImg.shape)
        frameImg = frameImg[deslocat[2]:deslocat[2]+desheight,deslocat[0]:deslocat[0]+deswidth,:]
        # print(frameImg.shape)
        outvideo.write(frameImg)
        # cv.waitKey(1000/int(fps))
    outvideo.release()
    capture.release()
    print("cut video done:-----------------\n")

    mixVideo(videofile,cvdesvideo,desvideo)

    return 1

def mixVideo(audioVideo,imageVideo,desvideo,destime):
    print("combine audio and video start:------"+audioVideo+"-------"+imageVideo+"\n")

    auv = VideoFileClip(audioVideo).subclip(destime[0],destime[1])
    audio = auv.audio
    if imageVideo==None:
        auv = auv.set_audio(audio)
    else:
        video = VideoFileClip(imageVideo).subclip(destime[0], destime[1])
        auv = video.set_audio(audio)
    auv.write_videofile(desvideo)
    print("save combined video .......done\n")

def test(test):
    cap = cv.VideoCapture(test)
    width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    # 以下三种都可以,参数为保存的文件名，编码格式，帧率，图片大小，色彩模式（默认为FALSE灰度图片）
    writer1 = cv.VideoWriter('myresult.avi', cv.VideoWriter_fourcc(*'DIVX'), cap.get(cv.CAP_PROP_FPS), (width, height),
                             True)
    writer2 = cv.VideoWriter('myresult.avi', cv.VideoWriter_fourcc(*'MJPG'), cap.get(cv.CAP_PROP_FPS), (720, 404),
                             True)
    writer3 = cv.VideoWriter('/Users/jintaoduan/Downloads/myresult.mp4', cv.VideoWriter_fourcc(*'mp4v'),
                             cap.get(cv.CAP_PROP_FPS), (width, height),
                             True)
    for i in range(int(60 * round(cap.get(cv.CAP_PROP_FPS)))):  # 截取1分钟
        _, frame = cap.read()
        writer3.write(frame)
    cap.release()
    writer3.release()

def test1(test,desvideo):
    videotarget = VideoFileClip(test)
    videotarget.write_videofile(desvideo)

# editvideo by parse video filename,like filename format test=0=10=400=1200=0=x.mp4
def editVideoDir(srcDir,cvDir,desDir):
    filelist = listdir(srcDir)
    for filename in filelist:
        namelist = filename.split(".")[0].split("=")
        name = namelist[0]
        destime = (int(namelist[1]),int(namelist[2]))
        srcfile = srcDir+filename
        cvfile = cvDir+name+str(destime[1]-destime[0])+"_noAudio.mp4"
        desfile = desDir+name+str(destime[1]-destime[0])+".mp4"
        if len(namelist)==7:
            desloc = (int(namelist[3]),int(namelist[4]),int(namelist[5]),-1 if namelist[6]=="x" else int(namelist[6]))
            editVideo(srcfile,cvfile,desfile,destime,desloc)
        if len(namelist==3):
            mixVideo(srcfile, None, desfile, destime)


# filename format test=0=10.mp4
def cutVideoDir(srcDir,desDir):
    filelist = listdir(srcDir)
    for filename in filelist:
        namelist = filename.split(".")[0].split("=")
        name = namelist[0]
        destime = (int(namelist[1]), int(namelist[2]))
        srcfile = srcDir+filename
        desfile = desDir+name+str(destime[1]-destime[0])+".mp4"
        mixVideo(srcfile,None,desfile,destime)


if __name__ == '__main__':
    test = '/Users/jintaoduan/Downloads/20作业安排.mp4'
    cvdesvideo = '/Users/jintaoduan/Downloads/20作业安排cvres.mp4'
    desvideo = '/Users/jintaoduan/Downloads/20作业安排testres000.mp4'
    desvideo2 = '/Users/jintaoduan/Downloads/testres2.mp4'
    desvideo3 = '/Users/jintaoduan/Downloads/testres3.mp4'
    # res = editVideo(test,cvdesvideo,desvideo,(0,10),(400,1200,0,-1))
    # print(res)
    # test1(desvideo3,desvideo3)
    # cutVideo(test,desvideo,(0,10))
    cvsrcDir='/Users/jintaoduan/Downloads/'
    cvcvDir='/Users/jintaoduan/Downloads/'
    cvdesDir='/Users/jintaoduan/Downloads/'
    srcDir='/Users/jintaoduan/Downloads/'
    desDir='/Users/jintaoduan/Downloads/'
    dirlist = [cvsrcDir,cvcvDir,cvdesDir,srcDir,desDir]
    for dirpath in dirlist:
        if os.path.exists(dirpath):
            os.makedirs(dirpath)
    editVideoDir(cvsrcDir,cvcvDir,cvdesDir)
    cutVideoDir(srcDir,desDir)




