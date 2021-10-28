import re
haslo=input("Wprowadź hasło: ")
wymagania = ['malalitera','duzalitera','liczba','znakspecjalny','miedzy6a16']
if re.search('[a-z]',haslo):
    wymagania.remove('malalitera')
if re.search('[A-Z]',haslo):
    wymagania.remove('duzalitera')
if re.search('[0-9]',haslo):
    wymagania.remove('liczba')
if re.search('["$","#","@"]',haslo):
    wymagania.remove('znakspecjalny')
if 5 < len(haslo) < 17:
    wymagania.remove('miedzy6a16')

print("\n\n\n\n")
if 'malalitera' in wymagania:
    print("Brakuje małej litery")
if 'duzalitera' in wymagania:
    print("Brakuje dużej litery")
if 'liczba' in wymagania:
    print("Brakuje liczby")
if 'znakspecjalny' in wymagania:
    print("Brakuje znaku specjalnego")
if 'miedzy6a16' in wymagania:
    print("Hasło ma albo mniej niż 6 znaków, albo więcej niż 16")
print("\n\n\n\n")



