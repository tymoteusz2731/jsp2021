a=int(input("Wprowadz 'a': "))
b=int(input("Wprowadz 'b': "))

while (a%b) != 0 and (b%a) != 0:
    if a>b:
        b = a%b
    else:
        a = b%a
else:
    if a>b:
        print("NWD to:", b)
    else:
        print("NWD to:", a)
