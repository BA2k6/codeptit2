for _ in range(int(input())):
    n = input()
    d = 0
    for i in range(2,len(n),2):
        if n[i] != n[0]:
            d = 1
            break
    if len(n) % 2 != 0 and n[0] != n[1] and d ==0:
        print("YES")
    else:
        print("NO")


