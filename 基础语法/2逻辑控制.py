#!/usr/bin/python3
# -*- coding: UTF-8 -*-

var1 = 10
sum = 0
counter = 1

'''if判断'''
if var1:
    print ("1 - if 表达式条件为 true")
elif not var1:
    print ("2 - if 表达式条件为 false")

'''while循环'''
while counter <= var1:
    sum = sum + counter
    counter += 1
else:
    print ("循环结束", counter, " 大于", var1)
    print("1 到 %d 之和为: %d" % (var1,sum))

'''for循环'''
for i in range(10):
    print(i)

list=[1,2,3,4]
'''迭代器, 可用于 子符串, 列表, 元组'''
it = iter(list)
print (next(it))