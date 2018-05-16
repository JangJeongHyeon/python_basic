def get_max_min(data_list):
    min = data_list[0]
    max = data_list[0]
    for i in data_list:
        if(min > i):
           min = i
        if(max < i):
           max = i
    return(min, max)


print("min: %d  max: %d" % get_max_min([1,2,3,9,4,5,6,7]))