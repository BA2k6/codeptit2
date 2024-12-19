for i in range(int(input())):
    x,y = map(int,input().split())
    if y == 1:
        if 0<x and x<20:
            print("Ma Ket")
        elif 20<=x and x<32:
            print("Bao Binh")
    elif y == 2:
        if 0<x and x <= 18:
            print("Bao Binh")
        elif 19 <=x and x <= 29:
            print ("Song Ngu")
    elif y ==3:
        if 0< x and x<=20:
            print ("Song Ngu")
        elif 21<= x and x <=31:
            print("Bach Duong")
    elif y ==4:
        if 0< x and x <= 19:
            print("Bach Duong")
        elif 20 <= x and x <=30:
            print("Kim Nguu")
    elif y ==5:
        if 0 < x and x <= 20:
            print ("Kim Nguu")
        elif 21 <= x and x <= 31:
            print ("Song Tu")
    elif y == 6:
        if 0 < x and x <= 20:
            print ("Song Tu")
        elif 21<= x and x <=30:
            print("Cu Giai")
    elif y == 7 :
        if 0 <x and x <= 22:
            print("Cu Giai")
        elif 23 <= x and x <= 31:
            print("Su Tu")
    elif y ==8:
        if 0 < x and x <= 22 :
            print("Su Tu")
        elif 23 <= x and x <= 31:
            print ("Xu Nu")
    elif y == 9 :
        if 0 < x and  x <= 22:
            print ("Xu Nu")
        elif 23 <= x and x <= 30:
            print("Thien Binh")
    elif y == 10:
        if 0 < x and x <= 22:
            print("Thien Binh")
        elif 23<= x and x <= 31:
            print("Thien Yet")
    elif y == 11:
        if 0 < x and x <= 22:
            print ("Thien Yet")
        elif 23 <= x and x <= 30:
            print ("Nhan Ma")
    elif y == 12:
        if 0 < x and x <= 21 :
            print("Nhan Ma")
        elif 22<= x and x <= 31:
            print ("Ma Ket")







