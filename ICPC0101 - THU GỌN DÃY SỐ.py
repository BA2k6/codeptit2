n= int(input())
a = list(map(int,input().split()))
b =[]
for i in a:
    if len(b) ==0:
        b.append(i)
    else:
        if (b[-1] + i) % 2 == 0:
            b.pop()
        else:
            b = b + [i]
print(len(b))






