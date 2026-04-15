n=1; s = 0; dem = 0
while n < 100: 
    for i in range (1, n + 1):
        if n % i == 0:
            s += 1
        if s == n :
            print (n, end=" ")
            dem += 1    
    n += 1
print ("Có", dem, "số hoàn hảo.")