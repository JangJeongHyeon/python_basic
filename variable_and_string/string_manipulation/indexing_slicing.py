# initialize string object
my_string = 'hello world'

# get string length
print(len(my_string))

# get 'hello' from my_string
# slice[begin_index:end_index], end_index is exclusive.
print(my_string[0:5])
# same result
print(my_string[:5])


# get 'world' from my_string
print(my_string[6:11])
# same result
print(my_string[6:])
# same result
print(my_string[7:-1])