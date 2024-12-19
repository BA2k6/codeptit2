from math import *
# kiểm tra số nguyên tố
def ham1(n):
    for i in range(2,isqrt(n)+1):
        if n % i == 0 :
            return False
    return n >1
# hàm tính tổng
def ham2(n):
    tong = 0
    while n != 0:
        tong += n %10
        n //= 10
    return tong
# tính tổng các chữ số chẵn
def ham3(n):
    tong = 0
    while n != 0:
        if n % 10 % 2 == 0:
            tong += n % 10
        n //= 10
    return tong
# tổng các số nguyên tố
def ham4(n):
    tong = 0
    while n != 0
        r = n % 10
        if r ==2 or r ==3 or r ==5 or r ==7:
            tong += r
        n //= 10
    return 10
# in ra số lật ngược của n
def ham5(n):
    rev = 0
    while n != 0:
        rev = rev*10 + n % 10
        n //=10
    return rev
# đếm ước là số nguyên tố
def ham6(n):
    dem = 0
    for i in range(2, isqrt(n)+1):
        if n % i ==0:
            dem+= 1
            while n%i ==0:
                n//=i
    if n > 1: dem += 1
    return dem
# in ước nguyen tố lớn nhất
def ham7(n):
    res = -1
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            res = i
            while n %i == 0:
                n //= i
    if n >1:
        res = n
    return res
# kiểm tra trong số có số 6 không
def ham8(n):
    while n != 0:
        if n % 10 ==6:
            return True
        n //= 10
    return False
# tính tổng giai thừa VD: 123 => 1! +2! +3!
def ham10(n):
    tong = 0
    while n != 0:
        tong += factorial(n%10)
        n//=10
    return tong
# kiểm tra xem 1 số có được tạo từ 1 chữ số hay không VD 6666 => True, 5556=> False
def ham11(n):
    donvi = n % 10
    while n != 0:
        if donvi != n % 10:
            return False
        n //=10
    return True
# tính tổng lũy thừa chữ số của n với số mũ là số chữ số VD: 123 => 1^3 + 2^3 + 3^3
def ham13(n):
    m = n
    dem = 0
    while n != 0:
        dem += 1
        n//=10
    tong = 0
    while m != 0:
        tong += (m%10)**dem
        m//=10
    return tong









