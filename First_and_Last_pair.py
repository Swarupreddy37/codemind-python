n = int(input())
a = list(map(int,input().split()))
for i in range(n // 2) :
    p = i
    q = n - i - 1
    print(a[p], a[q], end = " ")
if n % 2 != 0 :
    print(a[n // 2], 0)