n = int(input())
a = list(map(int,input().split()))
p = []
for i in range(n) :
    if a[i] % 2 == 0 :
        p.append(a[i])
for i in range(n) :
    if a[i] % 2 != 0 :
        p.append(a[i])
for i in range(n) :
    print(p[i], end = " ")