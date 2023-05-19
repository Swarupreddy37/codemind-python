n = int(input())
m = int(input())
a = max(n,m)
p = 0
r = 0
for i in range(1,a) :
    if n % i == 0 and i != n :
        p += i
    if m % i == 0 and i != m :
        r += i
if p == m and r == n :
    print("Amicable")
else :
    print("Not Amicable")