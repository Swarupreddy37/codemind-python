
def isprime(i : int) -> int :
    temp = i
    rev = 0
    while i != 0 :
        rem = i % 10
        rev = rev * 10 + rem
        i //= 10
    if rev == temp :
        return 1
    else :
        return 0

n = int(input())
for i in range(n - 1 , 1, -1) :
    if isprime(i) :
        a = i
        break
for i in range(n + 1,3 * n) :
    if isprime(i) :
        b = i
        break
if (n - a) > (b - n) :
    print(b)
elif (n - a) < (b - n) :
    print(a)
else :
    print(a, b)