n = input()
a = int(n[0]) * 10 + int(n[1])
b = int(n[3]) * 10 + int(n[4])
q = b * 6
p = a * 30 + b * 0.5
x = max(p, q) - min(p, q)
print(min(x, 360 - x))