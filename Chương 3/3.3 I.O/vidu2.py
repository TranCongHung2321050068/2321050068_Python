#nhập 1 dãy số nguyên gồm n phàn tử. Ghi dỹ số vừa nhập vào file "dulieu.txt" ở ổ đĩa C
n = int(input("nhập n: "))
obj = open("dulieu.txt", "w")
for i in range(n):
    x = int(input("nhập phần tử thứ " + str(i+1) + ": "))
    obj.write(str(x) + " ")
obj.close()