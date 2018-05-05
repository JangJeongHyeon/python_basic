def cal_upper(price):
    increment = price * 0.3
    return price + increment


def cal_lower(price):
    decrement = price * 0.3
    return price - decrement


author = 'JohnMark'

if(__name__ == "__main__"):
    print(cal_upper(10000))
    print(cal_lower(10000))
    print(__name__)