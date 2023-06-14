n = int(input())
p = list(map(int,input().split()))
a, b = map(int,input().split())
x = sum(p)
s = 0
for i in range(n) :
    if p[i] >= a and p[i] <= b :
        s += p[i]
print(x - s)