for _ in range(int(input())):
    a = input().strip()
    b=[]
    for i in range(1,len(a),2):
        k=a[i-1]*int(a[i])
        b.append(k)
    print("".join(b))
