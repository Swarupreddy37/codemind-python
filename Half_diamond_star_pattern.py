n = int(input())
if n <= 2 :
    print("The pattern is not possible")
else :
    
    for i in range(1, 2 * n) :
        if i <= n :
            p = i
        else :
            n -= 1
            p = n
        for j in range(p) :
            print('*', end = "")
        print()