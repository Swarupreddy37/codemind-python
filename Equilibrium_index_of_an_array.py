t = int(input())
for i in range(t) :
    n = int(input())
    a = list(map(int,input().split()))
    if n == 1 or n == 2 :
        print(-1)
    else :
        b = sum(a) - a[0]
        s = a[0]
        p = 0
        for j in range(1, n - 1) :
            b -= a[j]
            if s == b :
                p = j
                break
            s += a[j]
        if p :
            print(p)
        else :
            print(-1)