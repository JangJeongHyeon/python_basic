def add_start_to_end(start, end):
    sum = 0
    for i in range(start, end+1):
        sum += i

    return sum


if(__name__ == '__main__'):
    print(add_start_to_end(1,5))