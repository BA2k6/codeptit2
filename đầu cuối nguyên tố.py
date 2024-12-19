from math import sqrt
def nt(n):
    for i in range(2, int(sqrt(n))+1):
        if n%i ==0:
            return False
    return n > 1
for _ in range(int(input())):
    x = input()
    x1 = int(x[:3])
    x2 = int(x[-3:])
    if nt(x1) and nt(x2):
        print("YES")
    else:
        print("NO")