a=int(input("Wprowadź a: "))
b=int(input("Wprowadź b: "))
if a<b:
    c=a
    a=b
    b=c
Z=b%a
print(Z)
Z*=Z+3
print(Z)
