import os

# get current working directory
print(os.getcwd())

# get file and directory in the  specific path(default Path: current working directory)
print(os.listdir())

# get all file and directory name in c drive
print(os.listdir("c:"))

# count all file and directory
print(len(os.listdir()))
