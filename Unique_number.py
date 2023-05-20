n = int(input())
a = []
flag = 0
while n != 0 :
    rem = n % 10
    if rem not in a :
        a.append(rem)
    else :
        flag = 1
        break
    n //= 10
if flag == 1 :
    print("Not Unique Number")
else :
    print("Unique Number")