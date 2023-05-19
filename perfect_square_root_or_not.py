n = int(input())
flag = 0
for i in range (1, n) :
    if i * i == n :
        flag = 1;
    if i * i > n :
        break
if flag == 1 :
    print("True")
else :
    print("False")