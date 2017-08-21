#!/bin/env python
# -*- coding: utf-8 -*-

""" 
* author Zhecheng.Ma
* \last modified 2017-08-21 14:14:17
""" 
import thread
from time import sleep,ctime

loops = [4,2]
"""导入模块，并且定义loop函数，把常量放入这个函数之中"""
def loop(nloop,nsec,lock):
	print('start loop 0 at:',nloop,'at',ctime())
	sleep(nsec)
	print("loop",nloop,'done at',ctime())
	lock.release()
"""大部分工作在main（）中进行，这里设置了3个独立的for循环。首先创建一个锁的列表，通过使用thread.allocate_lock（）函数得到锁对象，然后通过acquire（）方法取得（每个锁）。
	取得锁的效果相当于‘把锁锁上’。一旦所伤后，就可以添加到锁列表locks中"""
def main():
	print("starting at:",ctime())
	locks=[]
	nloops = range(len(loops))
	
	for i in nloops:
		lock = thread.allocate_lock()
		lock.acquire()
		locks.append(lock)
	for i in nloops:
		thread.start_new_thread(loop,(i,loops[i],locks[i]))
	for i in nloops:
		while locks[i].locked():pass
	print("all DONE at:",ctime())
"""运行这个线程"""
if __name__ == '__main__':
	main()
