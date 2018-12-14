#coding=utf-8
'''
协程部分练习
'''
#1.	部署一个生产者-消费者管道，生产者会将值的平方发送给两个消费者。
#其中一个会储存并打印出 所发送的值中最小的一个，另一个则是最大的一个。
#======================
# 注意 变成generator的函数，在首次调用的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
def consumer1():
    L=[]
    r=''
    print('Consumer1Start')#只有第一次启动生成器的时候会运行该语句,之后再次调用生成器每次都是从yield处运行
    while True:
        n = yield r
        # 再次执行时从这里的yield继续执行, 将把produce传入的参数 n 赋给局部变量 n . 下轮循环再次遇到yield就会就将 r 返回给produce函数
        # 所以Python的yield不但可以返回一个值，它还可以接收调用者发出的参数(划重点)
        print('==%s'%n)# 由于生成器在启动的时候遇到上面的yield就返回了, 所以第一次不会执行这条语句. 之后每次都会被执行
        if not n:
            return
        L.append(n)
        print('消费者1======%s'%max(L))
        r = '200 OK' # 因为yield r 所以这个r会在下一次循环被返回给produce函数 
def consumer2():
    L=[]
    r=''
    print('Consumer2Start')
    while True:
        n = yield r
        if not n:
            return
        L.append(n)
        print('消费者2------%s'%min(L))
        r = '200 OK'
def producer(c):
    c.send(None)
    print('Producer Start')
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n**2) # # 获取生成器consumer中由yield语句返回的下一个值
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

if __name__=="__main__":
    A = consumer1()#并不会启动生成器,只是将A变成一个生成器
    B = consumer2()
    producer(A)
    producer(B)
