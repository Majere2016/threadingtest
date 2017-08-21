#!/bin/env python
# -*- coding: utf-8 -*-

""" 
* author Zhecheng.Ma
* \last modified 2017-08-21 17:16:54
""" 
import threading
from time import sleep,ctime

loops=[4,2]

class ThreadFunc(object):
	def __init__(self,func,args,name=''):
		self.name = name
		self.func = func
		self.args = args

	def __call__(self):
		self.func(*self.args)
	

def loop(nloop,nsec):
	print("start loop",nloop,"at:",ctime())
	sleep(nsec)
	print("loop",nloop,"done at:",ctime())

def main():
	print("starting at:",ctime())
	threads=[]
	nloops = range(len(loops))
	for i in nloops: #创建一个线程
		t = threading.Thread(target=ThreadFunc(loop,(i,loops[i]),loop.__name__))
		threads.append(t)
	for i in nloops: #开始进程
		threads[i].start()
	for i in nloops: #等待结束
		threads[i].join()
	print("all done at:",ctime())

if __name__ == "__main__":
	main()
