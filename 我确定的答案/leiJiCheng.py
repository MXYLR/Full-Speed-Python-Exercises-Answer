
#coding= utf-8

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
'''
使用之前定义的“Rectangle”类来进行下列练习：
1.	创建一个名为“Square”类，它是“Rectangle”的子类。 
2.	为“Square”写上构造方法。构造方法应只含x1,	y1两个坐标以及正方形的大小。记住，当你使 用“super”来调用“Rectangle”的构造方法时你仍会用到这些参数。
3.	实例化两个“Square”对象，调用	area	方法并打印这个对象。确保所有的计算返回的是正确的结 果，正方形的坐标始终与正方形的大小一致。
'''
class Square(Rectangle):
    def __init__(self):
        self.x1=int(input("正方形坐标x1:"))
        self.y1=int(input("正方形坐标y1:"))
        self.size=int(input("正方形的宽度:"))
        self.x2=self.x1+self.size
        self.y2=self.y1+self.size
        self.point1=[self.x1,self.y1]
        self.point2=[self.x2,self.y2]

if __name__=="__main__":
    a=Square()
    a.__str__()