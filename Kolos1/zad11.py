tablica=[]
dzwignia = True

while dzwignia == True:
    a = input("Wprowadź liczbę, zakończ wpisując 'end': ")
    if a == 'end':
        dzwignia = False
    else:
        try:
            a = int(a)
            tablica.append(a)
        except:
            print("To nie liczba - wartosć zostanie pominięta")


print("Oto liczby nieparzyste: \n")
for i in range(len(tablica)):
    if tablica[i] % 2 == 1:
        print(tablica[i])
