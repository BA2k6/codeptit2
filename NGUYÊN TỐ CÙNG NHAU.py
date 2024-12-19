import math
n,cs=input().split()
d=0
for i in range(10**(int(cs)-1),10**int(cs)):
    if math.gcd(int(n),i)==1:
        d+=1
        if d%10==0 :
            print(i)
        else:
            print(i,end=' ')
