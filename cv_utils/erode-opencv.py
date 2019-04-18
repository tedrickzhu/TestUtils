#encoding=utf-8
#author:Ethan
#software:Pycharm
#file:erode-opencv2.py
#time:2018/12/16 下午3:11

import cv2
import numpy as np
from os import listdir

def dilate():
    # img = cv2.imread('../images/vessel.jpeg',0)
    # cv2.imwrite('../images/vessel-gray.jpg',img)
    img = cv2.imread('../images/origin/im0162.png')
    print(type(img),img.shape)
    #腐蚀
    # kernele = np.ones((3,3),np.uint8)
    # erosion = cv2.erode(img,kernele,iterations = 1)
    # cv2.imwrite('../images/vessel-eroded2.jpg',erosion)

    kerneld = np.ones((5,5),np.uint8)
    dilotedimg = cv2.dilate(img,kerneld)
    cv2.imwrite('../images/vessel-rgb_dilated5.jpg',dilotedimg)

    # cv2.imshow('sourcegray',img)
    # cv2.imshow('erosion',erosion)
    # cv2.waitKey(0)
    # if cv2.waitKey(1) & 0xFF == ord('q'):

def resizemask():
    mask = cv2.imread('../images/fodus_mask.png')
    img = cv2.imread('../images/image_061.jpg')

    print('this is the shape of mask:',mask.shape)
    print('this is the shape of image:',img.shape)

def creat_mask(path,filename):
    img = cv2.imread(path+filename)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray',gray)
    print('this is the shape and type of gray: ',gray.shape,type(gray))
    ret, binary = cv2.threshold(gray, 70, 255,cv2.THRESH_BINARY)
    print('this is threshold value:',ret,type(binary),binary.shape)
    cv2.imwrite(path+filename.split('.')[0]+'_gray.jpg',gray)
    cv2.imwrite(path+filename.split('.')[0]+'_mask.jpg',binary)

    cv2.imshow('gray image',binary)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#全局阈值
def threshold_demo(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)  #把输入图像灰度化
    #直接阈值化是对输入的单通道矩阵逐像素进行阈值分割。
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
    print("threshold value %s"%ret)
    cv2.namedWindow("binary0", cv2.WINDOW_NORMAL)
    cv2.imshow("binary0", binary)

#局部阈值
def local_threshold(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)  #把输入图像灰度化
    #自适应阈值化能够根据图像不同区域亮度分布，改变阈值
    binary =  cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 25, 10)
    cv2.namedWindow("binary1", cv2.WINDOW_NORMAL)
    cv2.imshow("binary1", binary)


#用户自己计算阈值
def custom_threshold(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)  #把输入图像灰度化
    h, w =gray.shape[:2]
    m = np.reshape(gray, [1,w*h])
    mean = m.sum()/(w*h)
    print("mean:",mean)
    ret, binary =  cv2.threshold(gray, mean, 255, cv2.THRESH_BINARY)
    cv2.namedWindow("binary2", cv2.WINDOW_NORMAL)
    cv2.imshow("binary2", binary)

# src = cv2.imread('E:/imageload/kobe.jpg')
# cv2.namedWindow('input_image', cv2.WINDOW_NORMAL) #设置为WINDOW_NORMAL可以任意缩放
# cv2.imshow('input_image', src)
# threshold_demo(src)
# local_threshold(src)
# custom_threshold(src)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
def png2jpg(origin,dest):
    filelist = listdir(origin)
    for file in filelist:
        img = cv2.imread(origin+file)
        cv2.imwrite(dest+file.split('.')[0]+'.jpg',img)

if __name__ == '__main__':

    creat_mask('../images/','im0324.png')
    # # png2jpg('../images/origin/','../images/jpg/')
    # dilate()

    pass