#!/usr/bin/env python3
#coding= utf-8
'''
子字典部分练习:
先定义一个字典：
1.	students	=	{ 
2.	"Peter":	{"age":	10,	"address":	"Lisbon"}, 
3.	"Isabel":	{"age":	11,	"address":	"Sesimbra"}, 
4.	"Anna":	{"age":	9,	"address":	"Lisbon"}, 
5.	}
<hr/>
1.	“students”字典中有多少个同学？ 
2.	写一个函数接受“students”字典，返回平均年龄。 
3.	写一个函数接受“students”字典和一个地址（address）参数，
返回一个列表，内容是所有与 传入的地址相匹配的同学的名字。 
比如，调用	find_students(students,	'Lisbon')	
会返回	['Peter',	'Anna']	。
'''
students = {
"Peter":{"age":10,"address":"Lisbon"},
"Isabel":{"age":11,"address":"Sesimbra"},
"Anna":{"age":9,"address":"Lisbon"}
}



def getAverage(students):#年龄平均值
    sum=0
    for items in students:
            sum=sum+students[items]["age"]
            #这个地方是重点!!!!!!!!!!!!!
    return sum/len(students)



def find_students(students,address):
    L=[]
    for student in students:
        if students[student]["address"]==address:
            #这是调用子字典值的方式
            L.append(student)
    return L

if __name__=="__main__":
    print("该字典中有%d位同学"  %   len(students))#len()函数 不用多说了吧
    print("平均年龄为%d岁"  % getAverage(students))
    print(find_students(students,"Lisbon")  ,   "的地址为Lisbon")
#如果对这种调用方式还不明白,可以看看这个:https://blog.csdn.net/weixin_42373210/article/details/82218927


