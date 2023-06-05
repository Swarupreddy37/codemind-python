
def isprime(n : int ) -> bool :
    c = 0
    for j in range(2, n) :
        if n % j == 0 :
            c += 1
    if c :
        return False
    else :
        return True

n = int(input())
a = n // 2
c = 0
for i in range(2, a + 1) :
    if n % i == 0 :
        if isprime(i) :
            b = n // i
            d = i
            if isprime(b) :
                c = 1
                break
if c :
    print(d, b)
else :
    print("-1")