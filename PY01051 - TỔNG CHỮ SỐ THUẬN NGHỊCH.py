def check(n):
    if n == n[::-1] and len(n) > 1:
        return True
    else:
        return False
for _ in range(int(input())):
    n = input()
    t =0
    for i in n:
        t += int(i)
    t = str(t)
    if check(t):
        print("YES")
    else:
        print("NO")







