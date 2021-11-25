import trojkat

a = int(input("Wprowadź bok a: "))
b = int(input("Wprowadź bok b: "))
c = int(input("Wprowadź bok c: "))

tablica = []
tablica.extend([a,b,c])
sorted(tablica)
if tablica[0] + tablica[1] > tablica[2]:
    print("Obwód tego trójkąta to:", trojkat.obwod(a,b,c))
    print("Pole tego trójkąta to: ", trojkat.pole(a,b,c))
    print(trojkat.rowno(a,b,c))
    print(trojkat.prosty(a,b,c))
else:
    print("To nie jest trójkąt")