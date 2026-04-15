m = int (input ("Nhập số hàng:"))
n = int (input ("Nhập số cột:"))
matran = []
for i in range (m):
    hang = []
    for j in range (n):
        so = int ( input("Nhập phần tử thứ [" + str (i) + "][" + str (j) + "]:"))
        hang.append(so)
    matran.append(hang)

for i in range (m):
    for j in range (n):
        print (matran[i][j],end= " ")
    print ()