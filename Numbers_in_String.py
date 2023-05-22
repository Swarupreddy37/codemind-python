n = input()
s = 0
for i in n :
    if i >= '1' and i <= '9' :
        s += int(i)
print(s)