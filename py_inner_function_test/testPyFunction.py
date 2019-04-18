
# -*- coding: utf-8 -*-

#测试固定参数
'''
def add_list(L=[]):
	L.append('0')
	return L

print(add_list())
print(add_list())
print(add_list())
'''

#以杨辉三角为例测试生成器
'''
def triangle():
	L = [1]
	while True:
		yield L
		L.append(0)
		L = [L[i-1]+L[i] for i in range(len(L))]

		print('in the generator:',L)
k = 0
for j in triangle():
	if k ==5:
		break
	else:
		k+=1
		print('out of the generator；',j)
'''

#测试Python高级函数，map(),reduce()
'''
from functools import reduce
def normalize(name):
    name = name.lower()
    name = name[0].upper() +name[1:]
    return name

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(L):
	return reduce(lambda x,y:x*y,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
	print('测试成功!')
else:
	print('测试失败!')
'''
from functools import reduce

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)

print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))



#测试迭代器

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

now()

def logger(text='testparameter'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@logger('DEBUG')
def today():
    print('2015-3-25')

@logger()
def test():
	print('test parameters!')

test()

today()
print(today.__name__)


def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()

