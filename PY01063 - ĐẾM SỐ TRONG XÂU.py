def dem(s, n):
    dem = 0
    i = 0
    while i <= len(s) - len(n):
        if s[i:i + len(n)] == n:
            dem += 1
            i += len(n)
        else:
            i += 1
    return dem
for _ in range(int(input())):
    s = input().strip()
    n = input().strip()
    print(dem(s, n))