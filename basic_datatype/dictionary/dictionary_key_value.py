current_price = {'Daum KAKAO': 80000, 'naver':800000, 'daeshin':30000}

print(current_price)

# get all keys of dictionary object
# keys() function return type is not list object
print(current_price.keys())

# Should be change object type to list type
list(current_price.keys())

list_keys = list(current_price)
print(list_keys)


# Extract values of each item in the dictionary
list_value = list(current_price.values())
print(list_value)

# Check about Key exist in the dictionary
print('Samsung' in current_price.keys())

print('Daum KAKAO' in current_price.keys())


# Print value using by key
print(current_price['naver'])

# It will be occur error
print(current_price['Samsung'])