from math import isqrt
def nt(a):
    for i in range(2, isqrt(a)+1):
        if a% i == 1:
            return False
    return a >1
n = int(input())
a = [int(i) for i in input().split()]
b =[]
c=[b[1]]
d=[]
for j in a:
    if nt(j):
        b.append(j)
for z in range(1,len(b)):
    if b[z] != b[z-1]:
        c.append[b[z]]
for k in range(len(b)):







