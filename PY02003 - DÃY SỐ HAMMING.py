def check(b, x):
    l, r = 0, len(b) - 1
    while l <= r:
        m = (l + r) // 2
        if b[m] == x:
            return m + 1
        elif b[m] > x:
            r = m - 1
        else:
            l = m + 1
    return 0

b = set()
def Try(s):
    b.add(s)
    if 2 * s not in b and 2 * s <= 10 ** 18:
        Try(2 * s)
    if 3 * s not in b and 3 * s <= 10 ** 18:
        Try(3 * s)
    if 5 * s not in b and 5 * s <= 10 ** 18:
        Try(5 * s)
Try(1)
s = sorted(b)
for i in range(int(input())):
        n = int(input())
        if n not in b:
            print('Not in sequence')
        else:
            print(check(s, n))