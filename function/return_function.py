def cal_upper(price):
    increment = price * 0.3
    upper_price = price + increment
    return upper_price


def cal_lower(price):
    decrement = price * 0.3
    lower_price = price - decrement
    return lower_price


def cal_upper_lower(price):
    offset = price * 0.3
    upper = price + offset
    lower = price - offset
    return (upper, lower)


upper_price = cal_upper(1000)
lower_price = cal_lower(1000)
(upper, lower) = cal_upper_lower(10000)

print(upper_price)
print(lower_price)
print("*"*30)

print(upper)
print(lower)

