tong = 0
so = int (input ("Nhập số:"))
while so != 0 :
    if so % 2 == 0 :
        tong += so
    so = int (input ("Nhập số:"))
print ("Tổng các số chẵn là:", tong)