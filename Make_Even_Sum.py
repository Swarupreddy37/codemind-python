n = int(input())
a = list(map(int,input().split()))
c = 0
b = 0
for i in a:
    if i % 2 == 0 :
        c += 1
    else :
        b += 1
if c % 2 == 0 and b % 2 == 0 :
    print("1")
else :
    print("0")