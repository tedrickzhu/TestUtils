#encoding=utf-8
#author:Ethan
#software:Pycharm
#file:testPILImage.py
#time:2018/12/21 下午6:34

from PIL import Image

img = Image.open('../images/origin/im0162.png')

# 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
Img = img.convert('L')
Img.save("../images/test1.jpg")

# 自定义灰度界限，大于这个值为黑色，小于这个值为白色
threshold = 200

table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

# 图片二值化
print('this is the type of img gray:',type(Img))
photo = Img.point(table, '1')
photo.save("../images/test2.jpg")
