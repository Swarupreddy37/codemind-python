n = int(input())
a = list(map(int,input().split()))
b = sum(a)
for i in range(n,0,-1) :
    if b % i == 0 :
        print(i)
        break;