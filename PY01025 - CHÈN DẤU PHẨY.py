#cách 1
n = input()
for i in range(len(n)-3,0,-3):
    n = n[:i]+ "," + n[i:]
print(n)

#cách 2
n = int(input())  # Nhận một giá trị số nguyên từ người dùng
a = "{:,}".format(n)  # Định dạng số nguyên với dấu phẩy phân cách nghìn
print(a)  # In ra số đã được định dạng

