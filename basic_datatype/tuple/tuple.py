# list using '[' or ']' keyword for generating list object
# but tuple use '(' or ')' keyword. And tuple is can't change elements after generated.
# tuple is more faster than list

# generate tuple object
t = ('SAMSUNG', 'LG', 'SK')
print(t)

# Also tuple is use index for access elements.
print(t[0])
print(t[1])
print(t[2])

# test: change element value
# It will be comes up some error message.
t[0] = 'Naver'
