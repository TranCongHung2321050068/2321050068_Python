# Câu 7 Viết chương trình nhập vào một dãy số nguyên x1, x2, ..., xn (0 < n < 100), tính tổng các phần tử là số nguyên tố trong dãy, và kiểm tra xem tổng này có phải là số lẻ và lớn hơn 50 hay không.
# Hàm kiểm tra một số có phải số nguyên tố hay không
def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Hàm giải quyết chính cho Câu 7
def giai_cau_7(n):
    arr = []
    for i in range(n):
        so = int(input(f"Nhập phần tử thứ {i+1}: "))
        arr.append(so)

    tong_nt = 0
    for x in arr:
        if kiem_tra_nguyen_to(x):
            tong_nt += x
    
    print(f"Tổng các số nguyên tố là: {tong_nt}")
    
    # Kiểm tra điều kiện: số lẻ và > 50
    if tong_nt % 2 != 0 and tong_nt > 50:
        print("=> Thỏa mãn: Là số lẻ và lớn hơn 50.")
    else:
        print("=> Không thỏa mãn điều kiện.")

# Gọi module câu 7
# giai_cau_7()

# Câu 8 Viết chương trình nhập vào ba số nguyên dương x, y, z, sau đó tìm xem tích (x * y * z) có mấy chữ số và chữ số lớn nhất bằng bao nhiêu.


# Câu 9 Viết chương trình nhập vào ba số nguyên dương a, b, c, sau đó tính tổng (a + b + c) và kiểm tra xem trong tổng đó có bao nhiêu chữ số chẵn