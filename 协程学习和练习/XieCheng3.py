#coding=utf-8
#====================================================================================#
#2.	部署一个生产者-消费者管道，生产者会将值的平方发送给两个消费者，一次只发送给其中的一 个。 #
# 第一个值会发送给消费者1号，第二个则会发送给消费者2号，第三个又发送给消费者1号….           #
#  关闭生产者时会强制让消费者打印出它们所接收到的值的列表。                               #
#====================================================================================#
import time

def consumer1(name):

    L=[]
    try:
        while True:
            N=yield
            time.sleep(1)
            L.append(N)
            print("consumer %s"%name,"working")
            print("sonsumer %s recieve " % name,N)
            print("=======分割线======")
    except GeneratorExit:
        print("Consumer-%s has recieved"%name,L)
        
def consumer2(name):

    L=[]
    try:
        while True:
            N=yield
            time.sleep(1)#这个代码会让程序在这里停一会,用到了time模块
            L.append(N)
            print("consumer %s"%name,"working")
            print("sonsumer %s recieve " % name,N)
            print("=======分割线======")
            
    except GeneratorExit:
        print("Consumer-%s has recieved"%name,L)


def producer(G1,G2):
    n=0
    G1.send(None)
    G2.send(None)
    while n<5:
        G1.send(n**2)
        G2.send(n**2)
        n+=1
    G1.close()
    G2.close()


def main():
    t1=consumer1(1)
    t2=consumer2(2)
    producer(t1,t2)



if __name__=="__main__":
    main()
'''
让我解释该程序的运行过程:
程序从main()函数开始,
然后将t1 t2两个变量变成生成器,
再将t1 t2传入生产者producer,t1 t2对应生产者函数中的G1 G2;
接着生产者使用send(None)分别唤醒了生成器t1和t2,
接下来t1:
执行到yield处,函数暂停,接着跳到生产者,生产者G1.Send(n**2)将n的平方传到了yield处,并赋值给t1中的变量N;
然后消费者t1将N值添加进列表L,
执行        print("consumer %s"%name,"working")
            print("sonsumer %s recieve " % name,N)
            print("=======分割线======")
这三句代码后,该t2出场了,t2与t1情况一样;
最后生产者使用close()关闭了两个生成器,调用close()时会向对应的生成器抛出一个generatorExit异常,
然后两个生成器分别捕获了这个异常并执行了相应的except下面的代码.
'''