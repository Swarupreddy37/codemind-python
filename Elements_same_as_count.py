n = int(input())
a = list(map(int,input().split()))
b = []
for i in a :
    if i not in b :
        b.append(i)
x = 0
p = []
for i in b :
    c = a.count(i)
    if c == i :
        p.append(i)
        x = 1
if x :
    for i in p :
        print(i, end = " ")
else :
    print(-1)