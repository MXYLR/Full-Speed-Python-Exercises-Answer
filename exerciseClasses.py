#!/usr/bin/env python3
#coding= utf-8
class Rectangle:     
     def __init__(self,x1,y1,x2,y2):          
         self.x1 = x1         
         self.y1 = y1          
         self.x2 = x2          
         self.y2 = y2      
     def __str__(self):              
        return 'coordinate:%s,%s'%((self.x1,self.y1),(self.x2,self.y2))      
        def width(self):          
            width = abs(self.x1-self.x2)          
            return width      
     def height(self):          
         height = abs(self.y1-self.y2)          
         return height      
     def area(self):          
         return self.width()*self.height()     
     def circumference(self):         
         return 2*self.width()+2*self.height()  
a = Rectangle(1,1,3,3)  
print(a.area())  
print(a)