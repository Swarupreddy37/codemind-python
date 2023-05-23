n = int(input())
a = list(map(int,input().split()))
s1 = 0
s2 = 0
for i in a :
    if i % 2 == 0 :
        s1 += i
    else :
        s2 += i
print(max(s1,s2) - min(s1,s2))