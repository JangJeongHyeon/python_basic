import time

# check module 
print(dir(time))

# using time and ctime
print(time.time())
print(type(time.time()))
print(time.ctime())
print(type(time.ctime()))

# print year info
cur_time = time.ctime()
print(cur_time.split(' ')[-1])


# sleep every 1 seconds
for i in range(10):
    print(i)
    time.sleep(1)

