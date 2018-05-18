# create file object open with following path
file = open('/media/johnmark/DUMP/JJH/DevProject/python/Python_basic/file/buy_list.txt','rt')

# read lines in file
# readlines method is read each lines and return as list
lines = file.readlines()

print(lines)

# using loop
for line in lines:
    # print(line, end='')
    print(line.split('\n')[0])