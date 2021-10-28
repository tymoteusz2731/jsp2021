import math
a=int(input("Wprowadź a: "))
b=int(input("Wprowadź b: "))
c=int(input("Wprowadź c: "))
if a==0:
    print("To nie jest równanie kwadratowe!")
else:
    delta=b**2-4*a*c
    if delta == 0:
        x0 = -b/2
        print(" x0 = ", x0)
    elif delta < 0:
        print("Delta mniejsza od 0")
    else:
        x1=(-b-math.sqrt(delta))/2*a
        x2=(-b+math.sqrt(delta))/2*a
        print(' x1=', x1,"\n","x2 = ",x2)
    