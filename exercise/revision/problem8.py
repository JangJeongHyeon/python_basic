for i in range(0,5):
    # 왼쪽 공백 출력
    for j in range(i):
        print(" ",end="")
    # 가운데 별
    for h in range(0,9-i*2):
        print("*",end="")
    # 오른쪽 공백 출력
    for z in range(i):
        print(" ",end="")
    print()

# for j in range(5):
#     for i in range(j):
#         print(' ', end='')
#     for i in range(2*(5-j)-1):
#             print('*', end='')
#     print("")