n = int(input())
a = list(map(int, input().split()))
c = 0
for i in range(1, n - 1) :
    if a[i -1] % 2 == 0 and a[i + 1] % 2 == 1 or a[i - 1] % 2 == 1 and a[i + 1] % 2 == 0 :
        c += 1
if a[0] % 2 == 0 and a[n - 2] % 2 == 1 or a[0] % 2 == 1 and a[n - 2] % 2 == 0 :
    c += 1
if a[1] % 2 == 0 and a[n - 1] % 2 == 1 or a[1] % 2 == 1 and a[n - 1] % 2 == 0 :
    c += 1
print(c)