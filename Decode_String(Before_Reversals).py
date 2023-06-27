t = int(input())
for i in range(t) :
    a, b = map(int,input().split())
    n = input()
    while b :
        p = n[:b]
        x = p[::-1]
        q = n[b:]
        n = x + q
        b -= 1
    print(n)