n = int(input())
s = 0
while True :
    while n != 0 :
        rem = n % 10
        s += rem
        n //= 10
    if s < 10 :
        break
    n = s
    s = 0
print(s)