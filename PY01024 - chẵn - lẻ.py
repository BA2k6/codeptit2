def check(n):
    for i in range(len(n)):
        if int(n[i]) == int(n[i+1]) + 2 or int(n[i]) == int(n[i+1]) -2:
            return True
        else:
            return False
for _ in range(int(input())):
    n = input()
    t=0
    for i in n:
        t += int(i)
    if t % 10 ==0 and check(n):
        print("YES")
    else:
        print("NO")


