n = int(input())
a = list(map(int,input().split()))
b = []
for i in range(n - 1, n // 2 - 1, -1) :
    b.append(a[i])
for i in range(n // 2) :
    b.append(a[i])
for i in b :
    print(i, end = " ")