import functools
lista=[]
dzwignia= True
while dzwignia == True:
    a=input("Wprowadź liczbę (Wpisz 'end' jeżeli chcesz zakończyć): ")
    if a=="end":
        dzwignia = False
    else:
        lista.append(a)
wyniki = list(map(int, lista))
print("Mnożąc wszystkie wprowadzone elementy otrzymamy: ", functools.reduce(lambda a, b: a*b, wyniki))
print("Dodając wszystkie wprowadzone elementy otrzymamy: ",sum(wyniki))
