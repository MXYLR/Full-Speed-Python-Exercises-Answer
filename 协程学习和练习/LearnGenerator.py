def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        ret = yield a#如果第一次用next,那么这个a就是next前面变量的结果

        print(">>>ret>>>", ret)
        a, b = b, a+b
        current_num += 1

obj = create_num(10)

#obj.send(None) #send一般不会用来放到第一次启动生成器,如果非要这么做,那么传递None

ret = next(obj)
print(ret)

#send里面的数据会 传递给第5行,当做yield a 的结果,然后ret保存这个结果
#send的结果是下一次调用yield时,yield后面的值被赋给等号左边的ret
ret = obj.send("hahahaha")
print(ret)#这个print的结果就是yield返回的a的值了