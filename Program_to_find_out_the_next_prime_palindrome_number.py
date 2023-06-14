def ispalin(n : int) -> int :
    temp = n
    rev = 0
    while n > 0 :
        rem = n % 10
        rev = rev * 10 + rem
        n //= 10
    if rev == temp :
        return 1
    else :
        return 0
def isprime(n : int) -> int :
    c = 0
    for i in range(1, n + 1) :
        if n % i == 0 :
            c += 1
    if c == 2 :
        return 1
    else :
        return 0

n = int(input())
p = n + 1
while True :
    if ispalin(p) :
        if isprime(p) :
            print(p)
            break
    p += 1