import time
from multiprocessing.dummy import Pool

start_time = time.time()
str_list = ["w","q","e","r"]

def dayin(str):
    print("开始打印：",str)
    time.sleep(2)
    print("结束打印：",str)

# for st in str_list:
#     dayin(st)
#
# end_time = time.time()
#
# print("总耗时:",end_time-start_time)
pool = Pool(4)

pool.map(dayin,str_list)
end_time = time.time()
print("总耗时:",end_time-start_time)