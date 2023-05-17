n = int(input())
a = list(map(int,input().split()))
b = a.copy()
c = set(b)
x = 0
for i in c :
    d = a.count(i)
    if d == 1 :
        x += 1
        print(i,end=' ')
if x == 0:
    print("-1")