import asyncio
import time

urls = ["w","q","e","r"]

async def requst(url):
    print("正在下载：",url)
    await asyncio.sleep(2)
    print(url,"下载完成")

# 任务列表：需要存放多个任务对象
stacks = []
for url in urls:
    s = requst(url)
    task = asyncio.ensure_future(s)
    stacks.append(task)
start = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(stacks))
print(time.time()-start)