#1.7. Nhập/Xuất
#format()
name = "Trần Công Hùng"
msv = "2321050068"
lop = "DCCTCT68B"
print("Xin chào, tôi là {}, msv: {}, lớp: {}".format(name, msv, lop))

#1.8 Các kdl chuẩn
#1.8.1 Các hàm xử lý xâu
#Nhập vào 1 xâu "cnTt dia tin hoc, dia chat".Hthi xâu đó từ vtri 3, 4-7, all:
s = "cnTt dia tin hoc, dia chat, dia hoc"
print(s[3]) 
print(s[4:8])
print(s[:])
print(s[0:])
print(s[4:2:-1])
print(s[-1:-3:-1])
print(s[-3:-1])
#in:
print('a' in 'abc')
print('ac' in 'abc')
#Các hàm: len()
a = "dia"
print(len(a))
#lower(), upper()
print(a.lower())
print(a.upper())
#find()
print(s.find(a))
print(s.find(a, 10))
print(s.find(a, 20))
#count()
print(s.count(a))
print(s.count(a,10))
print(s.count(a,10, -1))
#replace()
print(s.replace("dia", "địa"))
print(s.replace("dia", "địa", 2))
#split()
print(s.split())
print(s.split(" ", 1))
#lstrip(), rstrip(), strip()
s1 = "   dia hoc   "
print(s1.lstrip())
print(s1.rstrip())
print(s1.strip()) 
#isalpha(), isdigit(), isspace()
print("abc".isalpha())
print("ab c".isalpha())
print("123".isdigit())
print("12 3".isdigit())
print("   ".isspace())
print(" .  ".isspace())

#1.8.2 List

