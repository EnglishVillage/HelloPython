#!/usr/bin/python
# -*- coding:utf-8 -*-

import math, functools, sys, types, logging, codecs,base64,struct,hashlib,itertools
import os, time, random, threading, multiprocessing, re
import tkMessageBox,socket
#这里不可以直接import Image
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from multiprocessing import Process, Pool, Queue
from collections import namedtuple,deque,defaultdict,OrderedDict,Counter
# from Tkinter import *

try:
	import cStringIO as StringIO
except ImportError:  # 导入失败会捕获到ImportError
	import StringIO
try:
	import json  # python >= 2.6
except ImportError:
	import simplejson as json  # python <= 2.5
# 序列化
try:
	import cPickle as pickle
except ImportError:
	import pickle

'a test.txt module'

__author__ = 'Wang kunzao'


# def test.txt():
# 	args = sys.argv
# 	if (len(args) == 1):
# 		print "hello world"
# 	elif (len(args) == 2):
# 		print 'Hello, %s!' % args[1]
# 	else:
# 		print 'Too many arguments!'

# if __name__ == '__main__':
# test.txt()



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



# 1.直接定义类
# class Student(object):
# 	def __init__(self, name, score):
# 		self.name = name
# 		self.score = score
#
# 	def print_score(self):
# 		print "%s:%s" % (self.name, self.score)
# bart=Student('Bart Simpson', 59)
# lisa=Student('Lisa Simpson', 87)
# bart.print_score()
# lisa.print_score()

# print type(Student)		#<type 'type'>
# print type(bart)		#<class '__main__.Student'>
# print type(lisa)		#<class '__main__.Student'>



# print type(123)
# print type('3')==types.StringType
# print type('王五')==types.UnicodeType	#False
# print type(None)==types.TypeType	#False
# #方法为type类型
# print type(str)==types.TypeType		#True



# 2.使用type定义类
# def fn(self,name='world'):
# 	print 'hello %s!' %(name)
# Hello= type('Hello', (object,), dict(hello=fn))
# h=Hello()
# h.hello()
# print type(Hello)
# print type(h)


# 获取对象所有方法
# print dir("asd")

# 底层调用__len__()方法
# print len("asd")







# 类
# class MyObject(object):
# 	def __init__(self):
# 		self.x = 9
# 	def power(self):
# 		return self.x * self.x
#
# obj=MyObject()
# print hasattr(obj,"x")
# print hasattr(obj,"y")
# print getattr(obj,"y","none")
# setattr(obj,"y","y")
# print getattr(obj,"y")
# #获取对象方法引用,可以执行
# print getattr(obj,"power")()




# class Student(object):
# 	pass
#
#
# s = Student()


# #动态绑定属性
# s.name="wkz"
# print s.name

# #动态绑定方法
# def set_age(self, age):  # 定义一个函数作为实例方法
# 	self.age = age
# #方法名,对象,类
# s.set_age=types.MethodType(set_age,s,Student)
# s.set_age(25)
# print s.age

# 给类动态绑定方法
# def set_score(self, score):
# 	print score
#
# Student.set_score=types.MethodType(set_score,None,Student)
# s2=Student()
# s2.set_score(99.9)
# s.set_score(99)





# #__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的：
# #除非在子类中也定义__slots__，这样，子类允许定义的属性就是自身的__slots__加上父类的__slots__。
# class StudentSlots(object):
# 	__slots__=('name','age')
#
# s=StudentSlots()
# s.name='wkz'
# s.age=25
# #s.score=100	#AttributeError: 'StudentSlots' object has no attribute 'score'
# print s.name,s.age#,s.score





# class Student(object):
# 	def __init__(self, name):
# 		self._name = name
#
# 	#重写toString()方法
# 	def __str__(self):
# 		return 'Student object (name: %s)' % self._name
#
# 	#debug输出
# 	__repr__ = __str__
#
# 	@property
# 	def birth(self):
# 		return self._birth
#
# 	@birth.setter
# 	def birth(self, birth):
# 		self._birth = birth
#
# 	@birth.deleter
# 	def birth(self):
# 		del self._birth
#
# 	@property
# 	def age(self):
# 		return 2017 - self._birth + 1

# s = Student('wkz')
# print s
# s.birth = 1993
# print s.birth
# print s.age
#
# # del s.birth
# s.birth = 1990
# print s.birth




# 斐波垃圾数列
# class Fib(object):
# 	def __init__(self):
# 		self._a, self._b = 0, 1
#
# 	def __iter__(self):
# 		return self
#
# 	def next(self):
# 		self._a, self._b = self._b, self._a + self._b
# 		if (self._a > 100000):
# 			raise StopIteration
# 		return self._a
#
# 	def __getitem__(self, n):
# 		if (isinstance(n, int)):
# 			a, b = 1, 1
# 			for x in range(n):
# 				a, b = b, a + b
# 			return a
# 		#切片的做的操作
# 		elif (isinstance(n, slice)):
# 			start = n.start
# 			stop = n.stop
# 			a, b = 1, 1
# 			L = []
# 			for x in range(stop):
# 				if (x >= start):
# 					L.append(a)
# 				a, b = b, a + b
# 			return L
#
# 	#找不到属性或者方法,则在这里寻找.
# 	#rest API可以使用这种方式
# 	def __getattr__(self, item):
# 		if(item=="age"):
# 			return lambda :25
# 		elif(item=="name"):
# 			return "wkz"
# 		raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)
#
# 	#调用对象本身
# 	def __call__(self, *args, **kwargs):
# 		print "这是斐波垃圾数列对象"




# f = Fib()
# for i in f:
# 	print i
# print f[0], f[1], f[5]
# print f[0:6]
# print f.name
# print f.age()

# f = Fib()
# # 判断对象是否可被调用
# print callable(f)
# print callable(Fib())
# print callable([1,3,5])
# print callable(None)
# #调用对象本身
# print f()





# 使用元类给class添加方法
# class ListMetaclass(type):
# 	def __new__(cls, name, bases, attrs):
# 		attrs['add']=lambda self,value:self.append(value)
# 		return type.__new__(cls, name, bases, attrs)
#
# class MyList(list):
# 	__metaclass__ = ListMetaclass
#
# L=MyList()
# #这个add方法,是通过metaclass中添加的
# L.add(1)
# print L


# 异常错误
# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
# 	try:
# 		bar('0')
# 	except Exception, e:
# 		#把错误记录到日志文件里
# 		logging.exception(e)
# 	finally:
# 		print 'finally...'
#
# main()
# print 'end'




# IO编程
# try:
# 	f=open("d:/tmp/wkz.txt","r")
# 	print f.read()
# except Exception,e:
# 	print e.message
# finally:
# 	f.close()

# 使用with操作IO,不用close.
# with open("d:/tmp/wkz.txt","r") as f:
# 	# print f.read(50)
# 	# print f.readline()
# 	for line in f.readlines():
# 		# 去掉前后空格
# 		print line.strip()

# rb是以二进制模式打开文件,读取文件可设置编码
# with open("d:/tmp/wkz.txt","rb") as f:
# 	print f.read().decode("utf8")

#
# with codecs.open("d:/tmp/wkz.txt","rb","gbk") as f:
# 	print f.read()

# with open("d:/tmp/wkz.txt","w") as f:
# 	f.write("wkz")








# print os.name
# # print os.uname()
# print os.environ
# print os.getenv("PATH")
# print os.path.abspath(".")
# #第2个路径不可加/
# print os.path.join("d:/tmp","sdf")
# os.mkdir("d:/aaa")
# os.rmdir('d:/aaa')
# print os.path.split("d:/tmp/wkz.txt")
# print os.path.splitext("d:/tmp/wkz.txt")
# os.rename("d:/tmp/wkz.txt","d:/tmp/wkz2.txt")
# os.remove("d:/tmp/wkz2.txt")
# 输出目录底下所有目录,打印不出来!!!???
# print [x for x in os.listdir("d:/tmp") if os.path.isdir(x)]






# 序列化
# d = dict(name='Bob', age=20, score=88)
# #任意对象序列化成一个str
# str=pickle.dumps(d)
# 保存序列化字符串到文件
# with open("d:/tmp/wkz.txt","w") as f:
# 	f.write(str)
# 从文件读取序列化文件
# with open("d:/tmp/wkz.txt","r") as f:
# 	d=pickle.load(f)
# 	print d




# 序列化成json
# d = dict(name='Bob', age=20, score=88)
# 序列化成json字符串
# str = json.dumps(d)
# 反序列为一个dict对象
# print json.loads(str)

# class Student(object):
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#
# s = Student('Bob', 20, 88)
# # print json.dumps(s)		#序列失败,因为不知道怎麽序列化
# str= json.dumps(s, default=lambda obj: obj.__dict__)
#
# def dict2student(d):
#     return Student(d['name'], d['age'], d['score'])
# #将json串反序列为对象需要一个转化
# print json.loads(str,object_hook=dict2student)#得到一个真正对象






# 进程相关
# #window无法运行
# print 'Process (%s) start...' % os.getpid()
# pid = os.fork()
# if(pid==0):
# 	print 'I am child process (%s) and my parent is %s.' %(os.getpid(),os.getppid())
# else:
# 	print 'I (%s) just created a child process (%s).' %(os.getpid(),pid)

# 使用Process创建1个子进程
# # 子进程要执行的代码
# def run_proc(name):
#     print 'Run child process %s (%s)...' % (name, os.getpid())
#
# #这个必须写在main函数底下
# if __name__=='__main__':
# 	print 'Parent process %s.' % os.getpid()
# 	p=Process(target=run_proc,args=('test.txt',))
# 	print 'Process will start.'
# 	p.start()
# 	p.join()
# 	print 'Process end.'

# # 进程池的方式批量创建子进程
# def long_time_task(name):
# 	print 'Run task %s (%s)...' % (name, os.getpid())
# 	start = time.time()
# 	time.sleep(random.random() * 3)
# 	end = time.time()
# 	print 'Task %s runs %0.2f seconds.' % (name, (end - start))

# # 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
# if __name__ == '__main__':
# 	print 'Parent process %s.' % os.getpid()
# 	p = Pool()
# 	for i in range(9):
# 		p.apply_async(long_time_task, args=(i,))
# 	print 'Waiting for all subprocesses done...'
# 	p.close()
# 	p.join()
# 	print 'All subprocesses done.'


# 进程间通信
# # 写数据进程执行的代码:
# def write(q):
#     for value in ['A', 'B', 'C']:
#         print 'Put %s to queue...' % value
#         q.put(value)
#         time.sleep(random.random())
#
# # 读数据进程执行的代码:
# def read(q):
#     while True:
#         value = q.get(True)
#         print 'Get %s from queue.' % value
#
# if __name__=='__main__':
#     # 父进程创建Queue，并传给各个子进程：
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入:
#     pw.start()
#     # 启动子进程pr，读取:
#     pr.start()
#     # 等待pw结束:
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()




# 多线程
# # 新线程执行的代码:
# def loop():
# 	print 'thread %s is running...' % threading.current_thread().name
# 	n = 0
# 	while n < 5:
# 		n += 1
# 		print 'thread %s >>> %s' % (threading.current_thread().name, n)
# 		time.sleep(1)
# 	print 'thread %s ended.' % threading.current_thread().name
#
# print 'thread %s is running...' % threading.current_thread().name
# t=threading.Thread(target=loop,name="LoopThread")
# t.start()
# t.join()
# print 'thread %s ended.' % threading.current_thread().name


# # 假定这是你的银行存款:
# balance = 0
# lock = threading.Lock()
#
# def change_it(n):
# 	global balance
# 	balance += n
# 	balance -= n
#
# def run_thread(n):
# 	for i in range(100000):
# 		# 先要获取锁:
# 		lock.acquire()
# 		try:
# 			change_it(i)
# 		finally:
# 			# 改完了一定要释放锁:
# 			lock.release()
#
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print balance


# 多线程没办法跑满所有CPU.【因为python的GIT】
# def loop():
# 	x = 0
# 	while True:
# 		x = x ^ 1
# print multiprocessing.cpu_count()
# for i in range(multiprocessing.cpu_count()):
# 	t=threading.Thread(target=loop)
# 	t.start()

# # 创建全局ThreadLocal对象:
# local_school = threading.local()
# def process_student():
# 	print 'Hello, %s (in %s)' %(local_school.student,threading.current_thread().name)
#
# def process_thread(name):
# 	# 绑定ThreadLocal的student:
# 	local_school.student=name;
# 	process_student()
#
# t1=threading.Thread(target=process_thread,args=("alice",),name="t1")
# t2=threading.Thread(target=process_thread,args=("bob",),name="t2")
# t1.start()
# t2.start()
# t1.join()
# t2.join()





# regex正则表达式
# if re.match(r"^\d{3}\-\d{3,8}$","010-12345"):
# 	print 1
# else:
# 	print 0
# 分组
# m=re.match(r"^(\d{3})\-(\d{3,8})$","010-12345")
# print m.group(0)
# print m.group(1)
# print m.group(2)
# 切分
# print re.split(r'[\s\,\;]+', 'a,b;; c  d')
# #贪婪匹配
# print re.match(r'^(\d+)(0*)$', '102300').groups()
# #非贪婪匹配
# print re.match(r'^(\d+?)(0*)$', '102300').groups()
# 编译
# re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# print re_telephone.match('010-12345').groups()
# print re_telephone.match('010-8086').groups()






# 带有名字的tuple
# Point = namedtuple('Point', ['x', 'y'])
# p=Point(1,2)
# print p.x,p.y
# print isinstance(p,tuple)
# print isinstance(p,Point)
#
# Circle = namedtuple('Circle', ['x', 'y', 'r'])



# deque
# q=deque(["a","b","c"])
# #插入到末尾
# q.append("x")
# #插入到开头
# q.appendleft("y")
# print q




# defaultdict
# dd=defaultdict(lambda :"N/A")
# dd["key1"]=123
# print dd["key1"]
# print dd["key2"]





# OrderedDict
# # d = {"a": 1, "b": 2, "c": 3}
# d = dict([('a', 1), ('b', 2), ('c', 3)])
# print d
# od = OrderedDict([("a", 1), ('b', 2), ('c', 3)])
# print od

#使用OrderedDict实现FIFO队列
# class LastUpdatedOrderedDict(OrderedDict):
# 	def __init__(self, capacity):
# 		super(LastUpdatedOrderedDict, self).__init__()
# 		self._capacity = capacity
#
# 	def __setitem__(self, key, value):
# 		containskey = 1 if key in self else 0
# 		if (len(self) - containskey >= self._capacity):
# 			last = self.popitem(last=False)
# 			print "remove:", last
# 		if (containskey):
# 			del self[key]
# 			print "set:", (key, value)
# 		else:
# 			print "add:", (key, value)
# 		OrderedDict.__setitem__(self, key, value)
#
#
# l = LastUpdatedOrderedDict(3)
# l["a"]=1
# l["b"]=1
# l["c"]=1
# l["d"]=1
# print l



#适用于Worldount
# c = Counter()
# for ch in 'programming':
# 	c[ch] = c[ch] + 1
# print c




#base64编码解码
# #编码
# print base64.b64encode("binary\x00string")
# #解码
# print base64.b64decode("YmluYXJ5AHN0cmluZw==")

# print base6004.urlsafe_b64decode('abcd--__')




#md5
# md5= hashlib.md5()
# md5.update("how to use md5 in python hashlib?")
# print md5.hexdigest()
# sha1算法
# sha1 = hashlib.sha1()
# sha1.update("how to use md5 in python hashlib?")
# print sha1.hexdigest()




#itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是迭代对象，只有用for循环迭代的时候才真正计算
#2是开始值,无限+1,一直执行
# natuals= itertools.count(2)
# ns = itertools.takewhile(lambda x: x <= 10, natuals)
# for n in ns:
# 	print n
# 	threading._sleep(1)

#无限重复字符串序列
# cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
# for c in cs:
# 	print c
# 	threading._sleep(1)

#重复指定次数的字符串【不指定次数，一直执行】
# repeat = itertools.repeat("Asdf", 10)
# for c in repeat:
# 	print c

#把一组迭代对象串联起来，形成一个更大的迭代器
# for c in itertools.chain("abc","def"):
# 	print c

#分组(后面可设置不区分大小写,不写则区分)
# for key,group in itertools.groupby("aAabBbccAA",lambda c:c.upper()):
# 	print key,list(group)

#跟map基本一样,
# imap()可以作用于无穷序列，并且，如果两个序列的长度不一致，以短的那个为准
# imap()返回一个迭代对象，而map()返回list
# for x in itertools.imap(lambda x,y:x*y,[10,20,30],itertools.count(1)):
# 	print x




#XML
#http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001407499098340324a6232bfee42348849d53c90576747000

# HTMLParser
# http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001407500818913cef22f247dbd4699921fe9d309727a20000









#PIL
#缩放50%
# 打开一个jpg图像文件，注意路径要改成你自己的:
im = Image.open('d:/tmp/aa.jpg')
# 获得图像尺寸:
w, h = im.size
# 缩放到50%:
im.thumbnail((w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('d:/tmp/thumbnail.jpg', 'jpeg')

#模糊效果
# im = Image.open('d:/tmp/aa.jpg')
# im2=im.filter(ImageFilter.BLUR)
# im2.save('d:/tmp/blur.jpg', 'jpeg')

#验证码
# # 随机字母:
# def rndChar():
#     return chr(random.randint(65, 90))
# # 随机颜色1:
# def rndColor():
#     return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
# # 随机颜色2:
# def rndColor2():
#     return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
# # 240 x 60:
# width = 60 * 4
# height = 60
# image = Image.new('RGB', (width, height), (255, 255, 255))
# # 创建Font对象:
# font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 36)
# # 创建Draw对象:
# draw = ImageDraw.Draw(image)
# # 填充每个像素:
# for x in range(width):
#     for y in range(height):
#         draw.point((x, y), fill=rndColor())
# # 输出文字:
# for t in range(4):
#     draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# # 模糊:
# image = image.filter(ImageFilter.BLUR)
# image.save('d:/tmp/code.jpg', 'jpeg');







#GUI程序,图形界面
# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.helloLabel = Label(self, text='Hello, world!')
#         self.helloLabel.pack()
#         self.quitButton = Button(self, text='Quit', command=self.quit)
#         self.quitButton.pack()
# app = Application()
# # 设置窗口标题:
# app.master.title('Hello World')
# # 主消息循环:
# app.mainloop()

# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.nameInput = Entry(self)
#         self.nameInput.pack()
#         self.alertButton = Button(self, text='Hello', command=self.hello)
#         self.alertButton.pack()
#
#     def hello(self):
#         name = self.nameInput.get() or 'world'
#         tkMessageBox.showinfo('Message', 'Hello, %s' % name)
# app = Application()
# # 设置窗口标题:
# app.master.title('Hello World')
# # 主消息循环:
# app.mainloop()







#socket编程
#TCP编程
# # 创建一个socket:
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 建立连接:
# s.connect(('www.sina.com.cn', 80))
# s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# # 接收数据:
# buffer = []
# while True:
#     # 每次最多接收1k字节:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = ''.join(buffer)
# # 关闭连接:
# s.close()
# header, html = data.split('\r\n\r\n', 1)
# print header
# # 把接收的数据写入文件:
# with open('d:/tmp/sina.html', 'wb') as f:
#     f.write(html)
# print data

# #服务器
# def tcplink(sock, addr):
#     print 'Accept new connection from %s:%s...' % addr
#     sock.send('Welcome!')
#     while True:
#         data = sock.recv(1024)
#         time.sleep(1)
#         if data == 'exit' or not data:
#             break
#         sock.send('Hello, %s!' % data)
#     sock.close()
#     print 'Connection from %s:%s closed.' % addr
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 监听端口:
# s.bind(('127.0.0.1', 9999))
# #指定等待连接的最大数量
# s.listen(5)
# print 'Waiting for connection...'
#
# while True:
#     # 接受一个新连接:
#     sock, addr = s.accept()
#     # 创建新线程来处理TCP连接:
#     t = threading.Thread(target=tcplink, args=(sock, addr))
#     t.start()
#
# #客户端
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 建立连接:
# s.connect(('127.0.0.1', 9999))
# # 接收欢迎消息:
# print s.recv(1024)
# for data in ['Michael', 'Tracy', 'Sarah']:
#     # 发送数据:
#     s.send(data)
#     print s.recv(1024)
# s.send('exit')
# s.close()



#UDP编程
# #服务端
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# # 绑定端口:
# s.bind(('127.0.0.1', 9999))
# print 'Bind UDP on 9999...'
# while True:
#     # 接收数据:
#     data, addr = s.recvfrom(1024)
#     print 'Received from %s:%s.' % addr
#     s.sendto('Hello, %s!' % data, addr)
# #客户端
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# for data in ['Michael', 'Tracy', 'Sarah']:
#     # 发送数据:
#     s.sendto(data, ('127.0.0.1', 9999))
#     # 接收数据:
#     print s.recv(1024)
# s.close()


