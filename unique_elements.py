n = int(input())
a = list(map(int,input().split()))
b = []
for i in range(n) :
    if a[i] not in b :
        b.append(a[i])
        print(a[i], end = " ")