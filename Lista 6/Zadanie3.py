def patrzimow(n):
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