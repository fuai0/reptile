import asyncio

# async修饰，调用返回协程对象
async def request(url):
    print(url)
    return url

# 创建协程对象
str1 = request("wang")

# 创建一个循环事件
loop = asyncio.get_event_loop()

# # 协程对象注册到循环事件loop当中,然后启动
# loop.run_until_complete(str1)


# task使用
# # 基于循环事件loop创建task对象
# task = loop.create_task(str1)
# print(task)
#
# # task注册到循环事件loop当中
# loop.run_until_complete(task)
# print(task)



# future使用
# 创建future对象
# task = asyncio.ensure_future(str1)
# print(task)
#
# # future注册到循环事件loop当中
# loop.run_until_complete(task)
# print(task)

# 绑定回调

def callback_func(task):
    # relust返回的就是task封装的协程对象对应函数的返回值
    print(task.result())


task = asyncio.ensure_future(str1)

# 回调函数绑定到task上
task.add_done_callback(callback_func)
loop.run_until_complete(task)