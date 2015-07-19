#coding:utf-8

#模块文档
"this is a template for python" 

#模块导入
import sys 
import os

#（全局）变量定义
debug = True 

#类定义（若有）
class FooClass(object): 
    "Foo Class"
	#pass
	
#函数定义
def test(): 
   "test function"
   foo = FooClass()
   if debug:
       print 'ran test()'
	   
#主程序	   
if __name__ == '__main__': 
    test()