#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 第一个注释
'''
第二注释
第三注释
'''

#数字,字符串
var = 1
str = 'Hello World!'
print ('字符串-------------------------------------') 
print (str)          # 输出完整字符串
print (str[0])         # 输出字符串中的第一个字符
print (str[2:5])       # 输出字符串中第三个至第五个之间的字符串
print (str[2:])        # 输出从第三个字符开始的字符串
print (str * 2)        # 输出字符串两次
print (str + "TEST")   # 输出连接的字符串

#列表 []
list1 = [ 'day', 2018 , 2.23, 'next', 70.2 ]
#嵌套列表 [[]]
list2 = [list1, [1, 2, 3]]
print ('列表-------------------------------------') 
print (list1[0])           # list第一个元素
print (list1[1:5])           # list第一个元素
print (list2)         # list2到6个元素


#元组 ()  元组与列表类似，元组的元素不能修改
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )  
print ('元组-------------------------------------') 
print (tuple[0])
print (tuple[1:5])

#字典 {键:值}
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
#相当于 dict = {'one': 'This is one', 2: 'This is two'}
print ('字典-------------------------------------') 
print (dict)                  # 输出完整的字典
print (dict.keys())           # 输出所有键
print (dict.values())         # 输出所有值
print (dict['one'])           # 输出键为'one' 的值
print (dict[2])               # 输出键为 2 的值

#集合{} 无序的不重复元素序列。
parame = {'a','a','b','c','d'}
parame1 = set('a')
parame1.add('b')
print ('集合-------------------------------------') 
print (parame)
print (parame1)
print (parame - parame1)