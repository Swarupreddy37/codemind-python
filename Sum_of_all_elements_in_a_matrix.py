n, m  = map(int,input().split())
s = 0
lst = [list(map(int,input().split())) for i in range(n)]
s = sum([sum(i) for i in lst])
print(s)
    