#encoding=utf-8

#测试装饰器
import functools

def log(func):
	#此行代码可以保持原有函数属性不变，如下面调用时的now函数，
	# 若无此行代码，则now的属性'__name__'则为wrapper
	@functools.wraps(func)
	def wrapper(*args,**kwargs):
		print('default text ,call %s():'%func.__name__)
		return func(*args,**kwargs)
	return wrapper

@log
def now():
	print('2018-08-08')

'''
此处调用now函数时，函数其实已经指向了log函数，将now函数作为一个参数传入了log函数，
所以会先执行log函数，在执行log函数时，也就是执行的是wrapper函数，最后才去执行now函数
'''
now()

#内容可以变化的装饰器
def logger(text='defaulttext'):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kwargs):
			print('%s  %s ():'%(text,func.__name__))
			return func(*args,**kwargs)
		return wrapper
	return decorator


#虽然有默认的传入参数，但是这里的括号不能省去
@logger()
def yesterday():
	print('yesterday!')

yesterday()

@logger('changetext')
def today():
	print('today!')

today()
