def kq(n):
    tong = 0
    tich = 1
    d = False
    for i in range(len(n)):
        x = int(n[i])
        if i % 2 != 0:
            tong +=x
        else:
            if x != 0:
                tich =tich* x
                d = True
    if d == False:
        tich = 0
    return tong, tich

for _ in range(int(input())):
    n = input().strip()
    tong, tich = kq(n)
    print(tich, tong)
