#coding=utf-8
'''
1.	写一个名为“squares”的生成器来生成（a）到（b）之间所有数的平方。
使用“for”循环来测试。 
2.	创建一个生成器来生成所有1到（n）之间的双数。 
3.	创建另一个生成器来生成所有1到（n）之间的单数。 
4.	创建一个生成器来生成所有（n）到0之间的数。 
5.	创建一个生成器来生成斐波那契数列。范围是第一个数字到（0）。
斐波那契数列的前几个数字是：	0,	1,	1,	2,	3,	5,	8,	13,	21,	34,	55,	89,	… 
6.	创建一个生成器来生成所有0到（n）之间所有的连续对。如（0,1）,(1,	2),	(2,	3)….
'''
#1.	写一个名为“squares”的生成器来生成（a）到（b）之间所有数的平方。
'''
一般地,我们用函数来实现该需求会这样做:
def squares(a,b):
    while a<b:
        i=a**2
        a+=1
        yield i
但如果用生成器来实现的话,只需将return改成yield即可
'''
def squares(a,b):
    while a<b:
        i=a**2
        a+=1
        yield i
#2.	创建一个生成器来生成所有1到（n）之间的双数。
def getEven(n):
    i=1#辅助变量
    while i<=n:
        if i%2==0:
            yield i
            i+=1
        else:
            i+=1
#3.	创建另一个生成器来生成所有1到（n）之间的单数。
def getOdd(n):
    i=1
    while i<=n:
        if i%2!=0:#将上面的==0改成!=0就行了
            yield i
            i+=1
        else:
            i+=1
#4.	创建一个生成器来生成所有（n）到0之间的数。 
def getN2Zero(n):
    while n>=0:
        yield n
        n-=1
#5.	创建一个生成器来生成斐波那契数列。范围是第一个数字到（0）。
#斐波那契数列的前几个数字是：	0,	1,	1,	2,	3,	5,	8,	13,	21,	34,	55,	89,	… 
def fibs(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n+=1
#6.	创建一个生成器来生成所有0到（n）之间所有的连续对。如（0,1）,(1,	2),	(2,	3)….
def getVector(n):
    i=0
    while i < n:
        L=[i,i+1]
        i+=1
        yield L

if __name__=="__main__":
    T1=squares(1,10)
    print(list(T1))
    T2=getEven(10)
    print(list(T2))
    T3=getOdd(10)
    print(list(T3))
    T4=getN2Zero(10)
    print(list(T4))
    T5=fibs(10)
    print(list(T5))
    T6=getVector(10)
    print(list(T6))