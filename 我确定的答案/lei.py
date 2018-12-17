#!/usr/bin/env python3
#coding: utf-8



#自行研究Python文档：	https://docs.python.org/3/tutorial/classes.html	完成下列 练习：
'''
1.	写一个名为“Rectangle”	的类，存储给定长方形的坐标（x1,	y1）,	(x2,	y2)。
2.	“Rectangle”类的构造方法接受4个参数（x1,	y1,	x2,	y2）以self关键字存储在类实例 中。 
3.	给它写一个	width()	方法和	height()	方法，分别返回这个长方形的宽和高。创建两 个“Rectangle”的实例对象来测试一下。 
4.	再写一个	area	方法，作用是返回这个长方形的面积（宽*高）。 
5.	最后写一个	circumference	方法，返回的是这个长方形的周长（宽*高*2）。 
6.	写一个	__str__	方法，其返回内容是长方形坐标(x1,y1)(x2,	y2)	。然后打印所创建的类实例中 的一个。
'''
class Rectangle:
    def __init__(self):
        self.x1=int(input("长方形坐标x1:"))
        self.x2=int(input("长方形坐标x2:"))
        self.y1=int(input("长方形坐标y1:"))
        self.y2=int(input("长方形坐标y2:"))
        self.point1=[self.x1,self.y1]
        self.point2=[self.x2,self.y2]
    def width(self):
        self.width=abs(self.x2-self.x1)
        return self.width
    def height(self):
        self.height=abs(self.y2-self.y1)
        return self.height
    def area(self):
        #返回面积
        return self.width*self.height
    def circumference(self):
        #返回周长
        return (self.width+self.height)*2
    def __str__(self):
        print("长方形坐标:",self.point1,self.point2)
        print("长方形的长:",self.width())
        print("长方形的宽:",self.height())
        print("长方形的面积:",self.area())
        print("长方形的周长:",self.circumference())
if __name__=="__main__":
    a=Rectangle()
    a.__str__()