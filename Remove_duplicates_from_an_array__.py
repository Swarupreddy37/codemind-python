n = int(input())
a = list(map(str, input().split()))
b = list(set(a))
b.sort()
for i in b :
    print(i, end = " ")