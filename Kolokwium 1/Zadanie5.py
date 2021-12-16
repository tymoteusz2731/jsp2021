tablica=[]
dzwignia = True

while dzwignia == True: # przyjmowanie liczb od użytkownika, które spelniają założenia
    a = input("Wprowadź liczbę, zakończ wpisując 'end': ")
    if a == 'end':
        dzwignia = False
    else:
        try:
            a = int(a)
            if a < 0:
                print("To nie jest liczba całkowita")
            else:
                tablica.append(a)
        except:
            print("To nie jest liczba bądź wprowadziłeś wartość po przecinku")

posrednia=[]
for i in tablica: # najpierw dodajemy i odejmujemy 1 od każdej wartości, wyniki dodajemy do nowej listy - posrednia
    posrednia.append(i+1)
    posrednia.append(i-1)

ostateczna = []
for i in range(len(posrednia)): # sprawdzamy czy wartość jest równa lub większa od zera, w innym wypadku, nie jest to liczba całkowita, zatem nie spełnia naszych wymagań
    if posrednia[i] >= 0:
        ostateczna.append(posrednia[i])

print(ostateczna)