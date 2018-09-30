#encoding=utf-8
#NumPy中，fft模块提供了快速傅里叶变换的功能。在这个模块中，许多函数都是成对存在的，也就是说许多函数存在对应的逆操作函数。例如，fft和ifft函数就是其中的一对。

import numpy as np
from matplotlib.pyplot import plot, show
x = np.linspace(0, 2 * np.pi, 30) #创建一个包含30个点的余弦波信号
wave = np.cos(x)
transformed = np.fft.fft(wave)  #使用fft函数对余弦波信号进行傅里叶变换。
print np.all(np.abs(np.fft.ifft(transformed) - wave) < 10 ** -9)  #对变换后的结果应用ifft函数，应该可以近似地还原初始信号。
plot(transformed)  #使用Matplotlib绘制变换后的信号。
show()