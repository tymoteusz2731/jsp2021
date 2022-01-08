def cyfrakontrolna(pesel):
    wspolczynnikwagowy = 1
    suma = 0
    suma += int(pesel[0])
    suma += int(pesel[1])*3
    suma += int(pesel[2])*7
    suma += int(pesel[3])*9
    suma += int(pesel[4])
    suma += int(pesel[5])*3
    suma += int(pesel[6])*7
    suma += int(pesel[7])*9
    suma += int(pesel[8])
    suma += int(pesel[9])*3
    suma = 10 - (int(suma) % 10)
    if suma == 10:
        suma = 0
    suma = str(suma)
    return suma


def sprawdzenie(i):
    if i[-2] != cyfrakontrolna(i):
        print("Błędny pesel")
    else:
        if int(i[2] + i[3]) > 12:
            miesiac = int(i[2] + i[3]) - 20
            rok = "2" + "0" + i[0] + i[1]
        else:
            miesiac = int(i[2] + i[3])
            rok = "1" + "9" + i[0] + i[1]
    dzien = int(i[4]+i[5])
    if int(i[9]) in [0,2,4,6,8]:
        plec = 'kobieta'
    else:
        plec = 'mezczyzna'
    
    return f"nr PESEL: {i}\n data urodzenia: {str(dzien)+'-'+str(miesiac)+'-'+str(rok)};\t płeć: {plec} \n"


f = open("pesel.txt", "r")
g = open("pesel2.txt", "x")
faa=f.readlines()
for i in faa:
    g.write(sprawdzenie(i))
f.close()
g.close()