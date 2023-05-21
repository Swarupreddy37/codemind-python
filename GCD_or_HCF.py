n, m = map(int, input().split())
p = min(n,m)
for i in range(p, 0, -1) :
    if n % i == 0 and m % i == 0 :
        break
print(i)