a, b, c = map(int,input().split())
p = 2 * a * b * c * 512
print(p // 1024, end = "")
print("KB")