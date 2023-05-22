t = int(input())
for i in range(t) :
    n, a, b, k = map(int,input().split())
    c = a * b
    cnt = n // a
    cnt += n // b
    cnt -= n // c
    if cnt >= k :
        print("Win")
    else :
        print("Lose")