#!/usr/bin/python
# -*- coding:utf-8 -*-

import math
import functools
import sys

try:
	import cStringIO as StringIO
except ImportError:  # 导入失败会捕获到ImportError
	import StringIO
try:
	import json  # python >= 2.6
except ImportError:
	import simplejson as json  # python <= 2.5

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


# if __name__ == '__main__':
	# test()



# # name = raw_input('please enter your name: ')
# # print name
# print "hello python", 213l
# print "ds", 23


# birth = int(raw_input('birth: '))
# if birth < 2000:
#     print '00前'
# else:
#     print '00后'


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



# dict和set中key元素不可以包含list对象,因为key是不可变的,list是可变
# dict={(1, 2, 3):"a",(1, [2, 3]):"2"}	#TypeError: unhashable type: 'list'
# print dict
# set=set([(1, 2, 3),(1, [2, 3])])	#TypeError: unhashable type: 'list'
# print set



# 遍历得到一个元组(元组包含角标和元素)
# for _ in enumerate(['A', 'B', 'C']):
# 	print _


# def fib(max):
# 	n, a, b = 0, 0, 1
# 	while n < max:
# 		print b
# 		# 下面那句等于底下3句[囧]
# 		# a, b = b, a + b
# 		temp = a + b
# 		a = b
# 		b = temp
# 		n = n + 1

# fib(6)





# #生成器:
# def fib2(max):
# 	n, a, b = 0, 0, 1
# 	while n < max:
# 		yield b
# 		a, b = b, a + b
# 		n = n + 1

# for i in fib2(6):
# 	print i



# 高阶函数
# def add(x,y,f):
# 	return f(x)+f(y)
#
# print add(-5,6,abs)


# 将数字转化为字符串,再转化为字符串
# print map(int,map(str,range(1,10)))

# print sum(range(11),2)
# map里面的函数只接收一个输入参数
# reduce里面的函数只接收2个输入参数
# print reduce(lambda x, y: x + y, map(lambda x: x+10, range(11)))
# 首字母大写,其它小写
# print map(lambda x:x[:1].upper()+x[1:].lower(),['adam', 'LISA', 'barT'])
# print reduce(lambda x, y: x * y, range(1, 5))




# print filter(lambda x:x%2==0,range(11))



# print sorted([1,2,5,2,3,4])




# def reversed_cmp(x, y):
#     if x > y:
#         return -1
#     if x < y:
#         return 1
#     return 0
# cmp是判断如何比较大小
# print sorted([36, 5, 12, 9, 21], cmp=reversed_cmp)
# reverse:True降序,False升序(默认)
# print sorted([36, 5, 12, 9, 21], reverse=True)




# def cmp_ignore_case(s1, s2):
#     u1 = s1.upper()
#     u2 = s2.upper()
#     if u1 < u2:
#         return -1
#     if u1 > u2:
#         return 1
#     return 0
# #忽略大小写进行字符串排序
# print sorted(['bob', 'about', 'Zoo', 'Credit'],cmp=cmp_ignore_case)


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




# 闭包中返回的函数引用了具体值,所以值不同
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
# # print int2('110000')
# print int2('110000',base=16)


class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
		print "%s:%s" % (self.name, self.score)

bart=Student('Bart Simpson', 59)
lisa=Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
