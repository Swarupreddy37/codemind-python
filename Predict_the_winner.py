n = int(input())
a = list(map(int,input().split()))
s1 = 0
s2 = 0
for i in range(n) :
    if i % 2 == 0 :
        s1 += a[i]
    else :
        s2 += a[i]
if s1 >= s2 :
    if (s1 - s2) % 4 == 0:
        print("X")
    else :
        print("Y")
else :
    if (s2 - s1) % 4 == 0:
        print("X")
    else :
        print("Y")