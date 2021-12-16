tablica=[]
liczby=[]
dzwignia = True

while dzwignia == True:  # dodawanie elementów
    a = input("Wprowadź liczbę, zakończ wpisując 'end': ")
    if a == 'end':
        dzwignia = False
    else:
        tablica.append(a)

for i in range(len(tablica)):  #sprawdzanie czy jest przynajmniej jedna liczba
    if tablica[i].isnumeric() == True:
        dzwignia = True
        break

for a in tablica:  # osobna tablica tylko z liczbami
    try:
        liczby.append(int(a))
    except:
        pass

if dzwignia == False:
    print("Nie ma wartości numerycznych")
else:
    maksimum = max(liczby)
    minimum = min(liczby)

if dzwignia == True:
    if maksimum == minimum:
        print("Nie ma największej wartości")
    else:
        print("Indeks największego elementu liczby: ", tablica.index(str(maksimum)))
        print("Indeks najmniejszego elementu liczby: ", tablica.index(str(minimum)))