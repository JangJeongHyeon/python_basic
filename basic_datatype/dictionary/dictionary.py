# Dictionary is save each data using by pair of key and value

# Make dictionary type object using by '{' or '}' keyword
current_price = {}

# Check data type using 'type()' function.
print(type(current_price))

# Add new item with key
current_price['daeshin'] = 30000

# Check result
print(current_price)

# Add another item with key
current_price['DaumKAKAO'] = 80000

# Check result
print(current_price)

# Length of dictionary object
print(len(current_price))

# Dictionary type object is not support indexing.
# print(current_price[0])


# Extract specific item using by key
print(current_price['DaumKAKAO'])