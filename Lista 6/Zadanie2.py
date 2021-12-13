import Szyfrowanie

tekst = input("Wprowadź tekst: ")
przesuniecie = int(input("Wprowadź przesunięcie: "))

print(Szyfrowanie.szyfrowanie(tekst,przesuniecie))
print(Szyfrowanie.deszyfrowanie(tekst,przesuniecie))
