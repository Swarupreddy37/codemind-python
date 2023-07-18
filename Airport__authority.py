n = int(input())
a = []
for i in range(n) :
    x = int(input())
    a.append(x)
k = int(input())
s = 0
for i in range(n) :
    if a[i] > k :
        s += 2
    else :
        s += 1
print(s)