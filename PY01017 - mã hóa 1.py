def mahoa(s):
    m = []
    d = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            d += 1
        else:
            m.append(f"{d}{s[i - 1]}")
            d = 1
    # Xử lý ký tự cuối cùng
    if len(s) > 0:
        m.append(f"{d}{s[-1]}")
    return ''.join(m)
kq = []
    # Đọc từng chuỗi và mã hóa
for _ in range(int(input())):
        s = input().strip()
        mh = mahoa(s)
        kq.append(mh)
for i in kq:
            print(i)

