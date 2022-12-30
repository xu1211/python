#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 第一个注释
'''
第二注释
第三注释
'''

'''
不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Set（集合）、Dictionary（字典）。
'''
#数字
var = 1

#字符串 ''
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
print (list1[1:5])           # list2到5个元素
print (list2)               # 嵌套list元素


#元组 ()  元组与列表类似，元组的元素不能修改
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
print ('元组-------------------------------------')
print (tuple[0])
print (tuple[1:5])

#集合 {}或set()， 无序的不重复元素序列。
parame = {'a','a','b','c','d'} # 创建有值集合
parame1 = set('a')  # 创建有值集合
parame1.add('b')
parame2 = set() # 创建空集合，不能用{}
print ('集合-------------------------------------')
print (parame)
print (parame1)
print (parame - parame1)

#字典 {键:值}
dict = {} # 创建字典
dict['one'] = "This is one"
dict[2] = "This is two"
#相当于 dict = {'one': 'This is one', 2: 'This is two'}
print ('字典-------------------------------------')
print (dict)                  # 输出完整的字典
print (dict.keys())           # 输出所有键
print (dict.values())         # 输出所有值
print (dict['one'])           # 输出键为'one' 的值
print (dict[2])               # 输出键为 2 的值