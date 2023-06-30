n = int(input())
a = list(map(int,input().split()))
b = sum(a) // n
s = 0
for i in a :
    if i <= b :
        s += 1
print(s)