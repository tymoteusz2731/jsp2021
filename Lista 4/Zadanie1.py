lista=[]
dzwignia= True
while dzwignia == True:
    a=input("Wprowadź liczbę (Wpisz 'end' jeżeli chcesz zakończyć): ")
    if a=="end":
        dzwignia = False
    else:
        lista.append(a)
wyniki = list(map(int, lista))
print("Dodając wszystkie wprowadzone elementy otrzymamy: ",sum(wyniki))

