n = int(input())
c = 0
for i in range(2, n) :
    if n % i == 0 :
        c += 1
if c or n == 1 :
    print("not a prime")
else :
    print("prime")