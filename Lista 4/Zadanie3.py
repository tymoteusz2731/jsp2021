import math
a=input("Wprowadź dane (zakończ literą 'R' jeżeli podajesz radiany, 'S' jeżeli stopnie): ")
lista=list(a)
if lista[-1] == "S":
    lista.pop()
    a=''.join(lista)
    a=math.radians(float(a))
    print(a)
elif lista[-1] == "R":
    lista.pop()
    a=''.join(lista)
    a=math.degrees(float(a))
    print(a)
else:
    print("Błąd składni")
