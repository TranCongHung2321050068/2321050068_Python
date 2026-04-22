#đọc file abcd.txt và in ra nd
obj = open("abcd.txt", "r")
nd1 = obj.read()
print('nd1: ' + nd1)
obj.close()
#có giá trị
obj = open("abcd.txt", "r")
nd2 = obj.read(6)
print('nd2: ' + nd2)
obj.close()

f =open("dulieu.txt", "r")
s = f.read()
s = s.strip()#xóa khoảng trắng ở đầu và cuối chuỗi s
a = s.split(" ") #tách chuỗi s thành 1 list a, mỗi phần tử của a là 1 số nguyên dưới dạng chuỗi
t=0
print("dãy:",a)
for i in a:
    t += int(i)
print("tổng:",t)
f.close()

#đọc file abcd.txt theo readline
obj = open("abcd.txt", "r")
nd4 = obj.readline()
print('nd4: ' + nd4)
obj.close()

obj = open("abcd.txt", "r")
nd5 = obj.readline(3)
print('nd5: ' + nd5)
obj.close()
#cách1  
obj = open("abcd.txt", "r")
for i in range(3):
    nd6 = obj.readline()
    print('nd6: ' + nd6)
obj.close()
#cách 2
obj = open("abcd.txt", "r")
nd7 = obj.readline()
while nd7: 
    print('nd7: ' + nd7)
    nd7 = obj.readline()
obj.close()
#cách 3
obj = open("abcd.txt", "r")
for i in obj:
    print(i)
obj.close()

#đọc vào 1 ma trận từ file matran.txt, tính và in ra tổng ma trận đó
f = open("matran.txt", "r")
s = f.readlines()
t = 0
for i in s:
    a = i.split() #tách chuỗi i thành 1 list a, mỗi phần tử của a là 1 số nguyên dưới dạng chuỗi
    for j in a:
        t += int(j)
print("tổng ma trận:", t)
f.close()  
