n, m = map(int,input().split())
a = list(map(int,input().split()))
c = 0
for i in range(len(a)) :
    s = 0
    for j in range(i,len(a)) :
        s += a[j];
        if s == m :
            c += 1;
print(c)