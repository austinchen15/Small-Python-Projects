def toBinary():
    import math
    binary = 0
    y = 0
    z = 0
    x = eval(input("Please input the number you would like converted to binary: "))
    for i in range(round(math.log2(x)),0,-1):
        y = (x % 2)*(10**z) + y
        x = x/2
        z = z + 1
    print(y)
