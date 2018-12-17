#coding=utf-8
#异步编程部分练习
'''
1.	写一个异步协同函数，它会将两个变量相加，并且会睡眠这些时间。使用异步循环来调用它。
2.	修改一下之前的那个程序，让它调度两次。
'''
import asyncio
#1.	写一个异步协同函数，它会将两个变量相加，并且会睡眠这些时间。使用异步循环来调用它。
async def add(x1,x2):
    X=x1+x2
    await asyncio.sleep(1)
    await add2(2,3)
    print('x1 + x2 =',X)
    return X
async def add2(x1,x2):
    X=x1+x2
    await asyncio.sleep(1)
    print('x1 + x2 =',X)
    return X


def main():
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(add(1,2))
    print(results)
    loop.close()
    ####
#2.	修改一下之前的那个程序，让它调度两次。

if __name__ == "__main__":
    main()