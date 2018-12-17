#!/usr/bin/env python3
#coding= utf-8
'''
字典部分练习:
先定义一个Python字典：
     1.	ages	=	{
     2.	"Peter":	10,
     3.	"Isabel":	11, 
     4.	"Anna":	9, 
     5.	"Thomas":	10, 
     6.	"Bob":	10, 
     7.	"Joseph":	11, 
     8.	"Maria":	12, 
     9.	"Gabriel":	10, 
     10.}
 1.	这个字典中有多少个同学？可以参考下len函数。 
 2.	写一个函数，接受“ages”字典作为参数，返回的是其中年龄的平均值。遍历字典中所有的项使用 的是items参数。 
 3.	写一个函数，接受“ages”字典作为参数，返回年龄最大的同学的名字。 
 4.	写一个函数，接受“ages”字典和数字“n”作为参数，返回的是一个新字典，新字典中每个同学的年龄均是“n”。
 比如，	new_ages(ages,	10)	返回的是“ages”字典的拷贝并且每个同学的年龄都是 10。
'''
ages = {
"Peter":10,
"Isabel":11,
"Anna":9,
"Thomas":10,
"Bob":10,
"Joseph":11,
"Maria":12,
"Gabriel":10
}

def getAverage(ages):#获取年龄平均值
    agesSum=0
    for items in list(ages.values()):#for循环求和
        '''
        字典的values()方法将字典中所有的值打包成一个迭代器,我们用list方法将其转为列表
        '''
        agesSum=agesSum+items
    return agesSum/len(ages)
#还有一种方法求年龄总和:sum(list(ages.values()))

def getOldest(ages):#返回年龄最大同学的名字
    Oldest=''#定义一个字符串变量,用于存储名字
    for items in list(ages.keys()):#字典的keys()方法将字典中所有的键打包成一个迭代器,我们用list转换为列表(其实不需要转换成列表,但是这里为了方便理解就这样了)
        if ages[items] == max(list(ages.values())):#for循环暴力查找,此处ages[items]返回items这个键所对应的值
            Oldest=items
    return Oldest

def new_ages(ages,n):
    for items in list(ages.keys()):#该语句的说明见上一个函数
        ages[items]=n#将n赋值给字典中的所有元素
    return ages
if __name__=="__main__":
    print("该字典中有%d个同学"%len(ages))
    Average=getAverage(ages)
    print("年龄平均值为:",Average)
    OldestName=getOldest(ages)
    print("年龄最大的同学名字是:",OldestName)
    N=new_ages(ages,10)
    print("转换后的字典为:",ages)
    