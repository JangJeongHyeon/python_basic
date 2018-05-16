# abs(number) return absolute value
print(abs(-3))


# chr(unicode) return character
print(chr(97)) 


# enumerate(sequence type variable) - return enumerate object(pair sequence number and element as sequence number)
for i, stock in enumerate(['Naver','KAKAO','SK']):
    print(i, stock)


# if no using enumerate functions
i = 0 
for stock in ['Naver','KAKAO','SK']:
    print(i, stock)
    i+=1


# id(object) is return primary value(memory address of object)
a = 1
b = 1
print(id(a))
print(id(b))


# len(s) is return number of elements
print(len(['SK','Naver']))
print(len((1,2,3)))
print(len({1:'sk',2:'Naver'}))


# list() is return list data
print(list('hello'))
print(list((1,2,3)))


# max() is return maxinum value
print(max(1,2,3))
print(max([1,2,3]))
print(min(1,2,3))
print(min([1,2,3]))


# sorted() is sort parameter object and return data as list
print(sorted((4,5,2,1,7,8,9)))
print(sorted([4,5,2,1,7,8,9], reverse=True))


# int() is change string to integer, str() is change integer to string
print(int('3'),type(int('3')))
print(str(3), type(str(3)))