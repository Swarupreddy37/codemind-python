n = int(input())
a = list(map(int,input().split()))
b = a.copy()
c = set(b)
x = 0
for i in c :
    p = a.count(i)
    x += (p // 2)
print(x)