def isprime(n : int) -> int :
    c = 0
    for i in range(1, n + 1) :
        if n % i == 0:
            c += 1
    if c == 2 :
        return 1
    else :
        return 0
        
n = int(input())
if isprime(n) :
    t = n
    rev = 0
    while t > 0 :
        rem = t % 10
        rev = rev * 10 + rem
        t //= 10
    if isprime(rev) :
        print("circular prime")
    else :
        print("prime but not a circular prime")
else :
    print("not prime")