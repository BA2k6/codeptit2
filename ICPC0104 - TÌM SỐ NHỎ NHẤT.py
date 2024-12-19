for _ in range(int(input())):
    x = input()
    a = ""
    for i in range(len(x)):
        if x[i].isdigit():
            a =a + x[i]
        else:
            a=a+ " "
    b = a.split()
    b = [int(num) for num in b]
    print(min(b))

