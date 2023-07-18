n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = []
b = a.copy()
for i in range(n) :
    c = m % n
    p = i + c
    if p >= n :
        p -= n
    b[p] = a[i]
for i in b :
    print(i, end = " ")