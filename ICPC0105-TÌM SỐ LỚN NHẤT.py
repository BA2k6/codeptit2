for _ in range(int(input())):
    x = input().strip()
    a = ""
    for i in range(len(x)):
        if x[i].isdigit():
            a =a + x[i]
        else:
            a=a+ " "
    b = a.split()
    b = [int(num) for num in b]
    print(max(b))

