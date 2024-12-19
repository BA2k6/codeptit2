def nt(n):
    kq='1'
    for i in range(2,int(n**0.5)+1):
        d=0
        if n%i!=0:
            continue
        while n%i==0:
            d+=1
            n//=i
        kq+= f" * {i}^{d}"
    if n>1:
        kq += f' * {n}^1'
    return kq
for _ in range(int(input())):
    n=int(input())
    print(nt(n))








