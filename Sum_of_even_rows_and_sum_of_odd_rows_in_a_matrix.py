n, m = map(int,input().split())
lst = [list(map(int,input().split())) for i in range(n)]
s1 = 0
s2 = 0
for i in range(n) :
    if i%2==0 :
        for j in range(m) :
            s1 += lst[i][j]
    else :
        for j in range(m) :
            s2 += lst[i][j]
print(s1,s2,end=' ')