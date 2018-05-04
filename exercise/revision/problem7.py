for i in range(5):
    for j in range(4-i):
        print(" ", end="")
    for z in range(i*2+1):
        print("*",end="")
    for z in range(4-i):
        print(" ", end="")
    print()
