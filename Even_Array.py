n = int(input())
a = list(map(int,input().split()))
c = 1
for i in a :
    if i % 2 != 0 :
        c = 0
        break
if c :
    print(True)
else :
    print(False)