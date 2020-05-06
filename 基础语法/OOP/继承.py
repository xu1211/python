#!/usr/bin/python3
# -*- coding: UTF-8 -*- 

import classDemo

'''子类student继承父类people'''
class student(classDemo.people):
    grade = ''
    def __init__(self,name,age,w,g):
        #调用父类的构函
        classDemo.people.__init__(self,name,age,w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        return (self.name, self.age, self.grade)

# 实例化类
y = student('李四', 19, 50, 100)

# 访问类的属性和方法
print("student 类的属性为：", y.name, y.age, y.grade)
print("student 类的方法 f 输出为：", y.speak())