import module1
x = int(input("Nhập chiều dài hình chữ nhật:"))
y = int(input("Nhập chiều rộng hình chữ nhật:"))
r = int(input("Nhập bán kính hình tròn:"))
z = int(input("Nhập cạnh hình vuông:"))
print("Diện tích hình chữ nhật:", module1.s_hcn(x, y))
print("Diện tích hình vuông:", module1.s_hv(z))
print("Chu vi hình chữ nhật:", module1.c_hcn(x, y))
print("Diện tích hình tròn:", module1.s_ht(r))