import os
from datetime import date
import fnmatch
path = input("Wprowadź ścieżkę do pliku: ")
przesuniecie = 0


def odczyt(path):
    stalasciezka = path
    for file_name in os.listdir(path):
        if fnmatch.fnmatch(file_name, 'plik_zaszyfrowany*'):
            for i in range(len(file_name)): # uzyskanie przesunięcia
                if file_name[i] == '%':
                    if file_name[i+2] == '%':
                        przesuniecie = int(file_name[i+1])
                        break
                    else:
                        przesuniecie = int(file_name[i+1] + file_name[i+2])
                        break
            path = f'{stalasciezka}\{file_name}' # pełna ścieżka do pliku
            with open(path, encoding="utf-8") as f: # czyń magię
                contents = f.read()
                zaszyfrowany = ''
                lista_odrzuconych = [' ',1,2,3,4,5,6,7,8,9,0,'','@','#','%','^','&','*','(',')','-','.',',','ą','ę','ó','ś','ć','ź','ż',':','ł','\n','–']
                for i in contents:
                    if i not in lista_odrzuconych:
                        if i.isupper():
                            i = i.lower()
                        if (ord(i)  - przesuniecie < 97):
                            zaszyfrowany += chr(ord(i) - przesuniecie + 26)
                        else:
                            zaszyfrowany += chr(ord(i) - przesuniecie)
                    else:
                        zaszyfrowany += i
    return zaszyfrowany

def zapis(contents):
    print(contents)
    path = input("Wprowadź ścieżkę zapisu: ")
    try: # jeżeli folder nie istnieje, utwórz go
        os.makedirs(path, exist_ok=False)
    except:
        pass
    d2 = date.today().strftime("%Y%m%d")
    path += f'\plik_deszyfrowany%{przesuniecie}%{d2}.txt'
    with open(path, 'w', encoding="utf-8") as F:
        F.write(contents)
    print("Gotowe!")

zapis(odczyt(path))


