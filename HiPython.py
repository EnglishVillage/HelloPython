#!/usr/bin/python
# -*- coding:utf-8 -*-

import math


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


def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x


def wkz_abs(x):
	if (x >= 0):
		return x
	elif (x < -1):
		return 1
	else:
		return -x


# 空函数
def nop():
	pass


# print abs(314)
# print wkz_abs(-123)
# print nop()


# 定义默认参数要牢记一点：默认参数必须指向不变对象！
def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
# print x, y
tuple = move(100, 100, 60, math.pi / 6)


# print tuple


# 可变参数,在参数前面加个*(>=0)
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum


# print calc(1,2,3,4)
# print calc(1,2,3)
# print calc()
nums = [1, 2, 3]


# print calc(*nums)	#已经有集合,则传进去的时候加个*


# c=0默认值,*args可变参数,**kw可变字典
def func(a, b, c=0, *args, **kw):
	print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw


# func(1, 2, 3, 'a', 'b', x=99,y="aa")

args = (1, 2, 3, 4)
kw = {'x': 99, 'y': "aa"}
# func('a','b','c',*args,**kw)


d = {'a': 1, 'b': 2, 'c': 3}
# 遍历dict的key
# for key in d:
# 	print key
# 遍历dict的value
# for value in d.itervalues():
# 	print value
# 遍历dict的key,value
# for k, v in d.iteritems():
# 	print k, v


#遍历得到一个元组(元组包含角标和元素)
# for _ in enumerate(['A', 'B', 'C']):
# 	print _

