tekst = "MCMLXXXVIII"
wynik = 0
bezpiecznik = True
jednosci = {
    "0": 0, "I": 1, "V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
x = list(tekst)

for i in range(len(x)):
    zmienna1 = x[i]
    try: 
        zmienna2 = x[i+1] # + 1 od aktualnej
        zmienna3 = x[i-1]
        if jednosci[zmienna2]>jednosci[zmienna1]: # jeżeli liczba poprzedzająca aktualną jest większa to od większej odejmnij mniejszą
            wynik = wynik + (jednosci[zmienna2] - jednosci[zmienna1])
        elif jednosci[zmienna1]>jednosci[zmienna3]:  # jeżeli aktualna zmienna jest większa od poprzedniej, oraz jest to pierwszy taki przypadek (Zawsze pierwsza liczba będzie pierwszym przypadkiem), dodaj i ustaw bezpiecznik na false
            if bezpiecznik == True:
                wynik = wynik + jednosci[zmienna1]
                bezpiecznik = False
        else:
            wynik = wynik + jednosci[zmienna1]
    except: # Jeżeli nie będzie zmiennej2 przeskocz tutaj i sprawdź: Czy liczba poprzedzająca była większa od aktualnej, jeżeli tak, dodaj aktualną liczbę do wyniku
        zmienna3 = x[i-1]
        if jednosci[zmienna1]<=jednosci[zmienna3]:
            wynik = wynik + jednosci[zmienna1]
        print(wynik)