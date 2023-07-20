n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = set(a)
p = []
x = 0
for i in b :
    c = a.count(i)
    if c == m :
        p.append(i)
        x = 1
if x :
    for i in p :
        print(i, end = " ")
else :
    print(-1)