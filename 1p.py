for _ in range(int(input())):
    p, q = map(int, input().split())
    x1 = input().strip()
    x2 = input().strip()

    # Thay thế chữ số p bằng q và ngược lại
    min_x1 = x1.replace(str(p), 'x').replace(str(q), str(p)).replace('x', str(q))
    max_x1 = x1.replace(str(p), 'y').replace(str(q), str(q)).replace('y', str(p))

    min_x2 = x2.replace(str(p), 'x').replace(str(q), str(p)).replace('x', str(q))
    max_x2 = x2.replace(str(p), 'y').replace(str(q), str(q)).replace('y', str(p))

    # Tính tổng nhỏ nhất và lớn nhất
    min_sum = int(min_x1) + int(min_x2)
    max_sum = int(max_x1) + int(max_x2)

    print(min_sum, max_sum)
