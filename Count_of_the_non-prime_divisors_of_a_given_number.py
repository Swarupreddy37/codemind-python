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
c = 1
for i in range(2, n + 1) :
    if n % i == 0 :
        if isprime(i) == 0 :
            c += 1
print(c)