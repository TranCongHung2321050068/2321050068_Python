n = int (input ("Nhập số pt dãy:"))
a = []
i = 0
while i < n :
    x = int (input ("Nhập số thứ " + str (i + 1) + ":"))
    a.append (x)
    i += 1
i = 0 
tong = 0
while i < n :
    if a [i] % 2 == 0 :
        tong += a [i]
    i += 1
print ("Tổng các số chẵn là:", tong)