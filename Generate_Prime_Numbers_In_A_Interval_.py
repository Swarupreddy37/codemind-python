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
m = int(input())
for i in range(n, m + 1) :
    if isprime(i) :
        print(i)