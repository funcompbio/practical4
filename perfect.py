x = int(input("Enter one value: "))
s = 0
i = 1
while (i < x) :
    if (x % i == 0) :
        s = s + i

    i = i + 1

if (s == x) :
    print("perfect")
else :
    print("not perfect")

