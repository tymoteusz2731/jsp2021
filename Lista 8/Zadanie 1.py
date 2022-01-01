import os
from datetime import date
path = input("Wprowadź ścieżkę do pliku: ")
przesuniecie = int(input("Wprowadź przesunięcie: "))


def odczyt(path,przesuniecie):
    try:
        with open(path, encoding="utf-8") as f:
            contents = f.read()
            zaszyfrowany = ''
            lista_odrzuconych = [' ',1,2,3,4,5,6,7,8,9,0,'','@','#','%','^','&','*','(',')','-','.',',','ą','ę','ó','ś','ć','ź','ż',':','ł','\n','–']
            for i in contents:
                if i not in lista_odrzuconych:
                    if i.isupper():
                        i = i.lower()
                    if ord(i) > 122 - przesuniecie:
                        zaszyfrowany += chr(ord(i) + przesuniecie - 26)
                    else:
                        zaszyfrowany += chr(ord(i) + przesuniecie)
                else:
                    zaszyfrowany += i
        return zaszyfrowany
    except:
        print("Coś poszło nie tak, upewnij się, że plik istnieje")




def zapis(contents,przesuniecie):
    path = input("Wprowadź ścieżkę zapisu: ")
    try: # jeżeli folder nie istnieje, utwórz go
        os.makedirs(path, exist_ok=False)
    except:
        pass
    d2 = date.today().strftime("%Y%m%d")
    path += f'\plik_zaszyfrowany%{przesuniecie}%{d2}.txt'
    with open(path, 'w', encoding="utf-8") as F:
        F.write(contents)
    print("Gotowe!")



zapis(odczyt(path,przesuniecie),przesuniecie)

