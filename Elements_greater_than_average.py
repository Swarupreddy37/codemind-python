n = int(input())
a = list(map(int,input().split()))
b = sum(a) // n
s = 0
for i in range(n) :
    if a[i] >= b :
        s += 1
print(s)