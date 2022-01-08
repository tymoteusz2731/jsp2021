import random
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
        


def pesel():
    # losowy rok z zakresu 1900 do 2399
    rok = random.randint(1900,2099)


    # losowy miesiąc pomnożony przez wielokrotność 20 jeśli jest taka potrzeba
    if rok <= 1999:
        miesiac = random.randint(1,12) #31dniowe : 1,3,5,7,8,10,12
    else:
        miesiac = random.randint(1,12) + 20 #31dniowe: 21,23,25,27,28,30,32
    
    #kontynuacja tworzenia daty - losowanie dnia

        #potrzebujemy rozróżnić na miesiace 30 i 31 dniowe

    miesiac31 = (1,3,5,7,8,10,12,21,23,25,27,28,30,32)
    miesiac30= (4,6,9,11,24,26,29,31)

    if miesiac in miesiac31:
        dzien = random.randint(1,31)
    elif miesiac in miesiac30:
        dzien = random.randint(1,30)
    else: # przypadek dla lutego
        if rok % 4 == 0: # gdy jest to rok przestępny
            dzien = random.randint(1,29)
        else:
            dzien = random.randint(1,28)
    
 
    szescdodziesiec = random.randint(1000,9999) # losowanie numeru serii oraz płci


    rok = str(rok)
    miesiac = str(miesiac)
    dzien = str(dzien)
    szescdodziesiec = str(szescdodziesiec)

    miesiac = miesiac.zfill(2) # uzupełnij zera na początku
    dzien = dzien.zfill(2)

    pesel = rok[2]+rok[3]+miesiac+dzien+szescdodziesiec
    print(pesel)
    pesel = pesel + cyfrakontrolna(pesel)
    return pesel

f= open("pesel.txt",'x')
for i in range(9):
    f.write(pesel()+"\n")
f.close()