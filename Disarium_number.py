n = int(input())
temp = n
s = 0
c = len(str(n))
while n != 0 :
    rem = n % 10
    s = s + (rem ** c)
    n //= 10
    c -= 1
if s == temp :
    print("True")
else :
    print("False")