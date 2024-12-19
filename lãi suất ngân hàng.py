from math import *
for _ in range(int(input())):
    N,X,M = map(float, input().split())
    nam = log(M/N, 1+X/100)
    print(ceil(nam))