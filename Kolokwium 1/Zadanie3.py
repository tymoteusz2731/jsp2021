import math

def pole(promien,jednostka):
    jednostki = ['mm','cm','m']
    if promien < 0:  # czy promień może być ujemny?
        return "Promień nie może być ujemny"

    area = math.pi * promien * promien  # obliczanie pola

    if jednostka not in jednostki:  # jeżeli jednostka jest inna niż jedna z trzech zdefiniowanych, wyrzuć błąd
        return "Zła jednostka"

    if jednostka == "mm":  # jeżeli podano inną jednostkę niż metr, przekonwertuj odpowiednio
        area = area * 1000000
    elif jednostka == "cm":
        area = area * 10000
    area = str(area) # zmień inta na stringa
    area = area + jednostka + "^2" # dodaj do wyniku jednostkę z dopiskiem ^2
    return area

print(pole(1,"m"))