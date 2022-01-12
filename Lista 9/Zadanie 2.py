import numpy as np
def statystyka(dane):
    print("Średnia: ", np.average(dane))
    print("Wariancja: ", np.var(dane))
    print("Odchylenie standardowe: ", np.std(dane), '\n')



statystyka([1,2,3,4,5,6])
plik=[]
f = open("dane.txt", "r")
plikroboczy=f.readlines()
for element in plikroboczy:
    plik.append(int(element.strip()))
f.close()
statystyka(plik)