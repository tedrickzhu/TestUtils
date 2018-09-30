#encoding=utf-8


import numpy as np
#a = np.array([[36,37,38],[37,49,61],[38,61,84]]) # 示例矩阵
#a = np.array([[14,26,22,16,22],
#              [26,50,46,28,40],
#              [22,46,50,20,32],
#              [16,28,20,20,26],
#              [22,40,32,26,35]])
c = np.array([[1,2,3],
              [3,4,5],
              [5,4,3],
              [0,2,4],
              [1,3,5]])

a =  c.dot(c.T)    
print(a)         
b = c.T.dot(c)
print(b)
 
A1 = np.linalg.eigvals(a)  # 得到特征值

print(A1)

A2,B = np.linalg.eig(a) # 其中A2也是特征值，B为特征向量
print('\n')
print(A2,B)

U, S, V = np.linalg.svd(c)

print('this is svd：')
print(U)
print('this is svd：')
print(S)
print('this is svd：')
print(V)

