<<<<<<< HEAD
﻿def patrzimow(n):
    if (n == 1):
        return "1"
    if (n == 2):
        return "11"

    aktualna = '11'
    for i in range(3,n+1):
        licznik = 1
        tymczasowa = ''
        aktualna += 'Ó'
        for j in range(1,len(aktualna)):
            if (aktualna[j] != aktualna[j-1]):
                tymczasowa += str(licznik)
                tymczasowa += aktualna[j-1]
                licznik = 1
            else:
                licznik += 1
        aktualna = tymczasowa
    return aktualna

print(patrzimow(3))
=======
def patrzimow(i):
    if i == 1:
        return "1"
    if i == 2:
        return "11"
    zmienna = '11'
    for a in range(3,i+1):
        ile_powtorzen = 1
        zmiennap = ''   
        for b in range(1,len(zmienna)):   
            if zmienna[b] != zmienna[b-1]:
                zmiennap = zmiennap + str(ile_powtorzen)
                zmiennap = zmiennap + zmienna[b-1]
                ile_powtorzen = 1
            else:
                ile_powtorzen = ile_powtorzen + 1
       zmienna = zmiennap
    return zmienna
print(patrzimow(5))
>>>>>>> 62266bbb5dc872b3c0f31c63a96a5208ff880438
