from math import isqrt
def nt(k):
    for i in  range(2, isqrt(k)+1):
        if k%i == 0:
            return False
    return k >1
n,m = map(int, input().split())
a = [list(map(int,input().split())) for i in range(n)]
for i in range(n):
    for j in range(m):
        if nt(a[i][j]):
            print(1,end = " ")
        else:
            print(0, end = " ")
    print()
