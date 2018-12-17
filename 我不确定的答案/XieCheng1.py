#coding=utf-8
'''
协程部分练习
1.	创建一个名为“square”的协程，它会打印出所发送的值的平方。 
2.	创建一个名为“minimize”的协程，它会保存并打印出所发送的值中最小的一个值。
'''
def square():
    print("square")
    while True:
        n=yield
        print(n**2)
def minimize(*args):
    r=''
    print("minimize")
    while True:
        n= yield r
        L=[]
        L.append(n)
        print(min(L))

if __name__=="__main__":
    X1=square()
    next(X1)
    X1.send(1)
    X1.send(2)
    X1.send(3)
    X1.close()
    X2=minimize()
    next(X2)
    X2.send(2)
    X2.send(3)
    X2.send(4)
    X2.send(1)