fo = open ("foo.txt", "w")
fo.write("Python la ngon ngu lap trinh. \nMinh cung nghi nhu the!! \n")
fo.close()
# Các thuộc tính của file:
#1 kiểm tra xem file đã đóng chưa
print(fo.closed)
#2 chế độ truy cập
print(fo.mode)
#3 tên file
print(fo.name)
