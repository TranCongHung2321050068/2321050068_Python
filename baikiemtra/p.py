# 1.1 Viết chương trình nhập vào một dãy số nguyên x1, x2, ..., xn (0 < n < 100),
    #  tính tổng các phần tử là số nguyên tố trong dãy, 
    # và kiểm tra xem tổng này có phải là số lẻ và lớn hơn 50 k
while True:
    n = int(input("Nhập số lượng phần tử n (0 < n < 100): "))
    if 0 < n < 100:
        break 
    else:
        print("Số n không hợp lệ. Vui lòng nhập lại!")
danh_sach_so = []  
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    danh_sach_so.append(x)  
tong_nguyen_to = 0
for x in danh_sach_so:
    la_so_nguyen_to = True  
    if x < 2:
        la_so_nguyen_to = False  
    else:
        for j in range(2, int(x**0.5) + 1):
            if x % j == 0:
                la_so_nguyen_to = False  
                break 
    if la_so_nguyen_to == True:
        tong_nguyen_to += x
print("\n--- KẾT QUẢ ---")
print(f"Tổng các số nguyên tố trong dãy là: {tong_nguyen_to}")
if tong_nguyen_to > 50 and tong_nguyen_to % 2 != 0:
    print("👉 Thỏa mãn: Tổng này LỚN HƠN 50 và là SỐ LẺ.")
else:
    print("❌ Không thỏa mãn điều kiện tổng lớn hơn 50 và là số lẻ.")
# 1.2 Viết chương trình nhập vào một dãy số thực x1, x2, …, xn (0 < n < 100), sau đó 
    # tìm trung bình cộng các phần tử âm trong dãy mà giá trị nằm trong khoảng (-1000, -10)
while True:
    n = int(input("Nhập số lượng phần tử n (0 < n < 100): "))
    if 0 < n < 100:
        break 
    else:
        print("Số n không hợp lệ. Vui lòng nhập lại!")
danh_sach_so = []
for i in range(n):
    x = float(input(f"Nhập phần tử thứ {i+1}: "))
    danh_sach_so.append(x)
tong_am = 0
dem_am = 0
for x in danh_sach_so:
    if x < 0 and -1000 < x < -10:
        tong_am += x
        dem_am += 1
print("\n--- KẾT QUẢ ---")
if dem_am > 0:
    trung_binh_cong_am = tong_am / dem_am
    print(f"Trung bình cộng các phần tử âm trong khoảng (-1000, -10) là: {trung_binh_cong_am}")
else:
    print("Không có phần tử âm nào trong khoảng (-1000, -10).")

# 1.3 Viết chương trình nhập vào một dãy số nguyên x1, x2, …, xn (0 < n < 200), 
    # tính tổng các phần tử chẵn trong dãy, và 
    # kiểm tra xem tổng này có chia hết cho 7 và nhỏ hơn 200 hay không
while True:
    n = int(input("Nhập số lượng phần tử n (0 < n < 200): "))
    if 0 < n < 200:
        break 
    else:
        print("Số n không hợp lệ. Vui lòng nhập lại!")
danh_sach_so = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    danh_sach_so.append(x)
tong_chan = 0
for x in danh_sach_so:
    if x % 2 == 0:
        tong_chan += x
print("\n--- KẾT QUẢ ---")
print(f"Tổng các phần tử chẵn trong dãy là: {tong_chan}")
if tong_chan % 7 == 0 and tong_chan < 200:
    print("👉 Thỏa mãn: Tổng này chia hết cho 7 và nhỏ hơn 200.")
else:
    print("❌ Tổng này không chia hết cho 7 và không nhỏ hơn 200.")

# 1.4 Viết chương trình nhập vào một dãy số thực x1, x2, …, xn (0 < n < 100), sau đó 
    # tìm trung bình cộng các phần tử dương trong dãy mà giá trị nằm trong khoảng (0, 1000)
while True:
    n = int(input("Nhập số lượng phần tử n (0 < n < 100): "))
    if 0 < n < 100:
        break 
    else:
        print("Số n không hợp lệ. Vui lòng nhập lại!")
danh_sach_so = []
for i in range(n):
    x = float(input(f"Nhập phần tử thứ {i+1}: "))
    danh_sach_so.append(x)
tong_duong = 0
dem_duong = 0
for x in danh_sach_so:
    if x > 0 and x < 1000:
        tong_duong += x
        dem_duong += 1
print("\n--- KẾT QUẢ ---")
if dem_duong > 0:
    trung_binh_cong_duong = tong_duong / dem_duong
    print(f"Trung bình cộng các phần tử dương trong khoảng (0, 1000) là: {trung_binh_cong_duong}")
else:
    print("Không có phần tử dương nào trong khoảng (0, 1000).")

# 2.1 Viết chương trình nhập vào ba số nguyên dương x, y, z, sau đó 
    # tìm xem tích (x * y * z) có mấy chữ số và chữ số lớn nhất bằng bao nhiêu.
x = int(input("Nhập số nguyên dương x: "))
y = int(input("Nhập số nguyên dương y: "))
z = int(input("Nhập số nguyên dương z: "))
tich = x * y * z
print("\n--- KẾT QUẢ ---")
print(f"Tích của x, y, z là: {tich}")
so_chu_so = len(str(tich))
chu_so_lon_nhat = max(str(tich))
max_chu_so = 0
    # for ky_tu in str(tich):
    #     so = int(ky_tu)
    #     if so > max_chu_so:
    #         max_chu_so = so
print(f"Số chữ số của tích là: {so_chu_so}")
print(f"Chữ số lớn nhất trong tích là: {chu_so_lon_nhat}")

# 2.2 Viết chương trình nhập vào ba số nguyên dương a, b, c, sau đó 
    # tính tổng (a + b + c) và kiểm tra xem trong tổng đó có bao nhiêu chữ số chẵn
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
c = int(input("Nhập số nguyên dương c: "))
tong = a + b + c
print("\n--- KẾT QUẢ ---")
print(f"Tổng của a, b, c là: {tong}")
so_chu_so = len(str(tong))
dem_chu_so_chan = 0
for ky_tu in str(tong):
    so = int(ky_tu)
    if so % 2 == 0:
        dem_chu_so_chan += 1
print(f"Số chữ số của tổng là: {so_chu_so}")
print(f"Số chữ số chẵn trong tổng là: {dem_chu_so_chan}")
# 3.1 Viết chương trình nhập vào 2 số nguyên dương a và b, sau đó 
    # kiểm tra xem a có chia hết cho chữ số nhỏ nhất của b hay không.
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
print("\n--- KẾT QUẢ ---")
chu_so_nho_nhat = min(str(b))
if chu_so_nho_nhat == '0':
    print("Chữ số nhỏ nhất của b là 0, không thể chia cho 0.")
else:
    chu_so_nho_nhat = int(chu_so_nho_nhat)
    if a % chu_so_nho_nhat == 0:
        print(f"a chia hết cho chữ số nhỏ nhất của b là {chu_so_nho_nhat}.")
    else:
        print(f"a không chia hết cho chữ số nhỏ nhất của b là {chu_so_nho_nhat}.")

# 3.2 Viết chương trình nhập vào 2 số nguyên dương m và n, sau đó 
    # tính tổng (a+b) và tìm ra chữ số lớn nhất trong tổng đó.
m = int(input("Nhập số nguyên dương m: "))
n = int(input("Nhập số nguyên dương n: "))
tong = m + n
print("\n--- KẾT QUẢ ---")
print(f"Tổng của m và n là: {tong}")
chu_so_lon_nhat = max(str(tong))
print(f"Chữ số lớn nhất trong tổng là: {chu_so_lon_nhat}")
#cách 2:
m = int(input("Nhập số nguyên dương m: "))
n = int(input("Nhập số nguyên dương n: "))
tong = m + n
print("\n--- KẾT QUẢ ---")
print(f"Tổng của m và n là: {tong}")
max_chu_so = 0
for ky_tu in str(tong):
    so = int(ky_tu)
    if so > max_chu_so:
        max_chu_so = so
print(f"Chữ số lớn nhất trong tổng là: {max_chu_so}")
#cách 3:
m = int(input("Nhập số nguyên dương m: "))
n = int(input("Nhập số nguyên dương n: "))
tong = m + n
print("\n--- KẾT QUẢ ---")
print(f"Tổng của m và n là: {tong}")
max_chu_so = 0
while tong > 0:
    chu_so = tong % 10
    if chu_so > max_chu_so:
        max_chu_so = chu_so
    tong //= 10
print(f"Chữ số lớn nhất trong tổng là: {max_chu_so}")

# 3.3 viết chg trình nhập 2 số nguyên dương m,n 
    # kiểm tra xem m có chia hết tổng chữ số của n k
m = int(input("Nhập số nguyên dương m: "))
n = int(input("Nhập số nguyên dương n: "))
print("\n--- KẾT QUẢ ---")
tong = 0
temp = n
while temp > 0:
    tong += temp % 10
    temp //= 10
if m % tong == 0:
    print(f"{m} chia hết cho tổng của chữ số {n} là {tong}.")
else:
    print(f"{m} không chia hết cho tổng của chữ số {n} là {tong}.")

# 4.1 viết chương trình nhập vào 1 số nguyên dương n, 
    # kiểm tra xem tổng các chữ số của n có phải là số chia hết cho 3 không?
n = int(input("Nhập n: "))
tong = 0
while n > 0:
    tong += n % 10
    n //= 10
if tong % 3 == 0:
    print("Tổng các chữ số chia hết cho 3")
else:
    print("Tổng các chữ số không chia hết cho 3")
# 4.2 viết chương trình nhập vào 1 số nguyên dương n, 
    # kiểm tra xem tích các chữ số của n có phải là số chẵn và lớn hơn 20 không?
n = int(input("Nhập n: "))
tich = 1
while n > 0:
    tich *= n % 10
    n //= 10
if tich % 2 == 0 and tich > 20:
    print("Tích các chữ số là",tich, "số chẵn và lớn hơn 20")
else:
    print("Tích các chữ số là",tich, "không thỏa mãn điều kiện")

