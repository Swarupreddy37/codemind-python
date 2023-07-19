n = int(input())
a = list(map(int,input().split()))
b = set(a)
p = 0
for i in b :
    c = a.count(i)
    if c == i :
        p += 1
print(p)