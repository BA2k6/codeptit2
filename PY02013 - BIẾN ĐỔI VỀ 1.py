while True:
    n = int(input())
    d = 1
    if n == 0: break
    while n !=1:
        if n % 2 == 0:
            n /= 2
        else: n = n*3 +1
        d += 1
    print(d)


