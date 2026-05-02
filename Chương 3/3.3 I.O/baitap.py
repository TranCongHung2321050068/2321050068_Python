#viết chương trình đọc tệp input.txt gồm n dòng, mỗi dòng là 1 số tự nhiên. kết quả chương trình là output gồm n dòng lần lượt là các ước số nguyên tố khác nhau
f = open("input.txt", "r")
fo = open("output.txt", "w")
s = f.readlines()
# for i in s:
#     num = int(i)
#     print("ước số nguyên tố của", num, "là: ")
#     for j in range(2, num + 1):
#         if num % j == 0:
#             kt = True
#             for k in range(2, int(j**0.5) + 1):
#                 if j % k == 0: 
#                     kt = False
#                     break
#             if kt:
#                 print(j, " ")
for line in s:
    n = int(line)
    k = 2
    while n>1:
        while n%k !=0:
            k+=1
        if n%k == 0:
            print(k,file = fo, end = " ")
            n = n//k
    print(file = fo)
f.close()
fo.close()


