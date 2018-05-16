import os

def get_txt_list(path):
    data = os.listdir(path)
    for f in data:
        if(f.endswith('.txt')):
            print(f)


get_txt_list('F:/JJH/DevProject/python/Python_basic/exercise/function_moudle')