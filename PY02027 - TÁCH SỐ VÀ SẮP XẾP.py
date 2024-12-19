a =""
for _ in range(int(input())):
    n = input()
    for i in n:
        if i.isdigit() :
            a = a + i
        else:
            a = a + " "
l = a.split()
x =[]
for i in l:
    k = int(i)
    x.append(k)
x.sort()
for i in x:
    print(i)



