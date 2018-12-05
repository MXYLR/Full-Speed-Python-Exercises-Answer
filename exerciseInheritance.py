#!/usr/bin/env python3
#coding=utf-8
class Square(Rectangle):
      def __init__(self,x1,y1,size):
          super().__init__(x1,y1,x1+size,y1+size)