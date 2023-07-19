n = int(input())
a = list(map(int,input().split()))
c = 1
for i in range(1, n, 2) :
    if a[i] % 2 == 0 :
        c = 0
if c :
    print(True)
else :
    print(False)