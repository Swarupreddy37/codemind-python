n = int(input())
a = list(map(int,input().split()))
p, q = map(int,input().split())
a.sort()
m = 0
for i in range(n) :
    if (a[i] < p and a[i] < q) or (a[i] > p and a[i] > q) :
        if m < a[i] :
            m = a[i]
if m :
    print(m)
else :
    print(-1)