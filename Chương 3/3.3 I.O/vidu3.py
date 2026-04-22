#Nhập vào 1 ma trận có m hàng và n cột. Ghi ma trận vừa nhập vào file "matran.txt" ở ổ đĩa C
m = int(input('Nhập số hàng:'))
n = int(input('Nhập số cột:'))
obj = open("matran.txt", "w")
for i in range(m):
    for j in range(n):
        x = int(input("Nhập phần tử thứ [" + str(i) + "][" + str(j) + "]: "))
        obj.write(str(x) + " ")
    obj.write("\n")
obj.close()