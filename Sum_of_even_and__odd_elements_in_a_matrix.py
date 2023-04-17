n, m = map(int,input().split())
lst = [list(map(int,input().split())) for i in range(n)]
s1 = 0
s2 = 0
for i in range(n) :
    for j in range(m) :
        if lst[i][j]%2 == 0 :
            s1 += lst[i][j]
        else :
            s2 += lst[i][j]
print(s1,s2)