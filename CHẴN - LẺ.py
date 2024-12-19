def kt(n):
    for i in range (1,len(n)):
        if abs(int(n[i]) - int(n[i - 1])) != 2:
            return False
    return True
for _ in range (int( input())):
    n = input()
    t = 0
    for i in n:
        t += int(i)
    if t % 10 != 0:
        print("NO")
    else:
        if kt(n):
            print("YES")
        else:
            print("NO")

