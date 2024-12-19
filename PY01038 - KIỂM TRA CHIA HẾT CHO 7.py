for _ in range(int(input())):
    x = input()
    x1 = x[::-1]
    i = 0
    while i <= 1000:
        i+=1
        if int(x) % 7 ==0:
            print(x)
            break
        t = int(x) + int(x1)
        x = str(t)
        x1= str(t)[::-1]
        if t % 7 == 0:
            print(t)
            break
    if i == 1001:
        print("-1")



