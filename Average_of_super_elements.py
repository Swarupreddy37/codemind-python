n = int(input())
a = list(map(int,input().split()))
b = set(a)
p = []
x = 0
for i in b :
    c = a.count(i)
    if c == i :
        p.append(i)
        x = 1
if x :
    print("%.2f"%(sum(p) / len(p)))
else :
    print(-1)