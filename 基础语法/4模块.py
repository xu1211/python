#!/usr/bin/python3
# -*- coding: UTF-8 -*-

'''一个.py文件就是一个模块,遇到 import 语句，如果模块在当前的搜索路径就会被导入'''
import fun
'''每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入'''
print (fun.__name__)
print ('模块内所有定义的名称:' , dir(fun))
print (fun.add(2,2))

'''只导入模块的指定部分,可以直接使用'''
from fun import add
print (add(3,3))
