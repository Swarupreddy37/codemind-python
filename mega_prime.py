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
c = 0
if isprime(n) :
    while n > 0 :
        rem = n % 10
        if isprime(rem) :
            c = 1
        else :
            c = 0
            break
        n //= 10
if c :
    print("Mega Prime")
else :
    print("Not Mega Prime")