def tong(x):
    t = 0
    for i in x:
        t += int(i)
    return t
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = [0]
    for x in a:
        if tong(x) < b[0]:
            b.insert(0,x)
        if tong(x) > 





