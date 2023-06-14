n = int(input())
a = list(map(int,input().split()))
p, q = map(int,input().split())
c = 1
for i in range(n) :
    if a[i] < p or a[i] > q :
        print(a[i], end = " ")
        c = 0
if c :
    print("-1")