#!/usr/bin/python
# -*- coding:utf-8 -*-

import math
import functools
import sys
try:
    import cStringIO as StringIO
except ImportError: # 导入失败会捕获到ImportError
    import StringIO
try:
    import json # python >= 2.6
except ImportError:
    import simplejson as json # python <= 2.5


'a test module'

__author__ = 'Wang kunzao'


def test():
	args = sys.argv
	if (len(args) == 1):
		print "hello world"
	elif (len(args) == 2):
		print 'Hello, %s!' % args[1]
	else:
		print 'Too many arguments!'

if __name__ == '__main__':
	test()



# # name = raw_input('please enter your name: ')
# # print name
# print "hello python", 213l
# print "ds", 23
#
# a = 100
# if a >= 0:
# 	print a
# else:
# 	print -a

# print r"""
# sdfsadf\n
# sdfsadf\t
# ds89
# """


# def my_abs(x):
# 	if x >= 0:
# 		return x
# 	else:
# 		return -x
#
#
# def wkz_abs(x):
# 	if (x >= 0):
# 		return x
# 	elif (x < -1):
# 		return 1
# 	else:
# 		return -x
#
#
# # 空函数
# def nop():
# 	pass


# print abs(314)
# print wkz_abs(-123)
# print nop()


# 定义默认参数要牢记一点：默认参数必须指向不变对象！
# def move(x, y, step, angle=0):
# 	nx = x + step * math.cos(angle)
# 	ny = y - step * math.sin(angle)
# 	return nx, ny


# x, y = move(100, 100, 60, math.pi / 6)
# # print x, y
# tuple = move(100, 100, 60, math.pi / 6)


# print tuple


# 可变参数,在参数前面加个*(>=0)
# def calc(*numbers):
# 	sum = 0
# 	for n in numbers:
# 		sum = sum + n * n
# 	return sum


# print calc(1,2,3,4)
# print calc(1,2,3)
# print calc()
# nums = [1, 2, 3]


# print calc(*nums)	#已经有集合,则传进去的时候加个*


# c=0默认值,*args可变参数,**kw可变字典
# def func(a, b, c=0, *args, **kw):
# 	print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw


# func(1, 2, 3, 'a', 'b', x=99,y="aa")

# args = (1, 2, 3, 4)
# kw = {'x': 99, 'y': "aa"}
# func('a','b','c',*args,**kw)


# d = {'a': 1, 'b': 2, 'c': 3}


# 遍历dict的key
# for key in d:
# 	print key
# 遍历dict的value
# for value in d.itervalues():
# 	print value
# 遍历dict的key,value
# for k, v in d.iteritems():
# 	print k, v


# 遍历得到一个元组(元组包含角标和元素)
# for _ in enumerate(['A', 'B', 'C']):
# 	print _

# def sum(*args):
# 	sum = reduce(lambda x, y: x + y, args)
# 	return sum
#
# print sum(*range(11))

# def lazy_sum(*args):
# 	def sum2():
# 		sum = reduce(lambda x, y: x + y, args)
# 		return sum
# 	return sum2


# print lazy_sum(*range(11))
# <function sum2 at 0x0000000002E7FCF8>

# lazy_sum(*range(11)):这是一个闭包函数,后面加个()代表执行
# print lazy_sum(*range(11))()

# print lazy_sum(*range(11))==lazy_sum(*range(11))
# False

# 闭包中返回的函数引用了变量i,所以值相同
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs
#
# f1, f2, f3 = count()
# print f1(),f2(),f3()
# 9 9 9

# 闭包中返回的函数引用了具体值
# def count2():
# 	ds=[]
# 	for i in range(1,4):
# 		def f(j):
# 			def g():
# 				return j*j
# 			return g
# 		ds.append(f(i))
# 	return ds
#
# f1, f2, f3 = count2()
# print f1(),f2(),f3()
# 1 4 9


# def dec(func):
# 	def wrapper(*args, **kv):
# 		print "zzz %s():" % func.__name__
# 		return func(*args, **kv)
# 	return wrapper
# 第1种:
# @dec
# def now():
# 	print '2017-03-17'
# print now()
# 第2种
# def now():
# 	print '2017-03-17'
# print dec(now)()




# 完整的装饰者
# def log(text):
# 	if(isinstance(text,str)):
# 		def dec(func):
# 			@functools.wraps(func)
# 			def wrapper(*args, **kv):
# 				print "%s %s():" % (text, func.__name__)
# 				return func(*args, **kv)
# 			return wrapper
# 		return dec
# 	else:
# 			@functools.wraps(text)
# 			def wrapper(*args, **kv):
# 				print "sss %s():" %text.__name__
# 				return text(*args, **kv)
# 			return wrapper
# 第1种写法:
# log的第1种用法
# @log("aaa")
# def now():
# 	print '2017-03-17'
# print now()
# log的第2种用法
# @log
# def now():
# 	print '2017-03-17'
# print now.__name__
# print now()
# 第2种写法
# def now():
# 	print '2017-03-17'
# log的第1种用法
# now = log('execute')(now)
# print now.__name__
# print log('execute')(now)()
# log的第2种用法
# print log(now)()


# 偏函数
# int2= functools.partial(int, base=2)
# print int2('110000')
