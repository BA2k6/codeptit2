l=[]
for _ in range( int(input())):
    k = input()
    if k not in l:
        l.append(k)
print(len(l))
