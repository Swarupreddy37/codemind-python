t = int(input())

def preprime(n : int) -> int :
    while n > 0 :
        c = 0
        for i in range(1, n + 1) :
            if n % i == 0:
                c += 1
        if c == 2 :
            return i
        n -= 1

def postprime (n : int) -> int :
    while True :
        c = 0
        for i in range(1, n + 1) :
            if n % i == 0:
                c += 1
        if c == 2 :
            return i
        n += 1
 
for i in range(t) :
    n = int(input())
    a = preprime(n)
    b = postprime(n + 1)
    if n - a > b - n :
        print(b)
    else :
        print(a)