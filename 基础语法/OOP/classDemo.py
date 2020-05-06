#!/usr/bin/python3
# -*- coding: UTF-8 -*- 

'''定义类'''
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性
    __weight = 0

    '''
    定义构造方法__init__
    类中所有的方法 必须包含参数self,且为第一个参数
    '''
    def __init__(self,name,age,w):
        self.name = name
        self.age = age
        self.__weight = w
    
    def speak(self):
        return (self.name, self.age, self.__weight)

# 实例化类
x = people('张三', 18, 50)

# 访问类的属性和方法
print("people 类的属性为：", x.name, x.age)
print("people 类的方法 f 输出为：", x.speak())