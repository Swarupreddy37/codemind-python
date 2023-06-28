t = int(input())
for i in range(t) :
    n = int(input())
    a = list(map(int,input().split()))
    b = a.copy()
    b.sort()
    if b == a :
        print(0)
    else :
        print(max(a) - min(a))