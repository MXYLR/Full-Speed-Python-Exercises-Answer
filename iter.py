#coding= utf-8
#迭代器部分练习
'''

1.	写一个迭代器类，返回的是所有“a”到“b”之间的数的平方。 
2.	写一个迭代器类，返回所有1到（n）之间的偶数。 
3.	写一个迭代器类，返回所有1到（n）之间的奇数。 
4.	写一个迭代器类，返回所有（n）到0之间的数。 
5.	写一个迭代器类，返回的是从第一个元素到（n）之间所有的斐波那契数列。
你可以回顾下函数部 分了解下什么是斐波那契数列。 
这是斐波那契数列的前几个数：0,	1,	1,	2,	3,	5,	8,	13,	21,	34,	55,	89,	...	。 
6.	写一个迭代器类，返回的是所有0到（n）的连续对，如（0,1）,(1,	2),	(2,	3)…。

'''
#1.	写一个迭代器类，返回的是所有“a”到“b”之间的数的平方。
class getPow:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __iter__(self):
        return self
    def __next__(self):
        if self.a>self.b:
            raise StopIteration
        i=self.a**2
        self.a=self.a+ 1
        return i

#2.	写一个迭代器类，返回所有1到（n）之间的偶数。
class getEven:
    '''
    直接定义一个变量,初始化值为2,然后一直加2.......暴力+2输出结果
    '''
    def __init__(self, n):
        self.n = n
        self.num = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.n:
            value = self.num
            self.num += 2
            return value
        else:
            raise StopIteration
#3.	写一个迭代器类，返回所有1到（n）之间的奇数。
class getOdd:
    def __init__(self,n):#self.num用于使迭代继续并返回结果
        self.n=n
        self.num=2
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= self.n:
            value = self.num-1#偶数减去1就是奇数了啦
            self.num += 2
            return value
        else:
            raise StopIteration
#4.	写一个迭代器类，返回所有（n）到0之间的数。
class getN2Zero:
    def __init__(self,n):#辅助变量self.num用于使迭代继续,self.num2用于返回结果
        self.n=n
        self.num=0
        self.num2=n
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=self.n:
            value=self.num2
            self.num2-=1
            self.num+=1
            return value
        else:
            raise StopIteration
#5.	写一个迭代器类，返回的是从第一个元素到（n）之间所有的斐波那契数列。
#你可以回顾下函数部 分了解下什么是斐波那契数列。 
#这是斐波那契数列的前几个数：0,	1,	1,	2,	3,	5,	8,	13,	21,	34,	55,	89,	...	。
class Fibs:
    def __init__(self,max):
        self.max=max
        self.a=0
        self.b=1
    def __iter__(self):
        return self
    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a,self.b, = self.b,self.a + self.b
        return fib
#6.	写一个迭代器类，返回的是所有0到（n）的连续对，如（0,1）,(1,	2),	(2,	3)…。
class getVector:
    def __init__(self,n):
        self.num=0
        self.n=n
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<self.n:
            self.num+=1
            L=[self.num-1,self.num]
            return L
        else:
            raise StopIteration
if __name__=="__main__":
    T1=getPow(0,10)
    print([ i for i in T1 ])
    T2=getEven(10)
    print([i for i in T2])
    T3=getOdd(10)
    print([i for i in T3])
    T4=getN2Zero(10)
    print([i for i in T4])
    T5=Fibs(10)
    print([i for i in T5])
    T6=getVector(10)
    print([i for i in T6])