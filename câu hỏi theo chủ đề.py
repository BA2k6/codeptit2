a = []
s = ''
for _ in range(int(input())) :
    s = input()
    a.append(s)
    if s == '' :
        n += 1
        print(a[0] + ':', len(a) - 2)
        a.clear()
print(a[0] + ':', len(a) - 1)