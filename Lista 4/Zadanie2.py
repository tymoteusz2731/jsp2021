lista=[]
dzwignia= True
while dzwignia == True:
    a=input("Wprowadź liczbę (Wpisz 'end' jeżeli chcesz zakończyć): ")
    if a=="end":
        dzwignia = False
    else:
        lista.append(a)
wyniki = list(map(int, lista))
for a in wyniki:
    if wyniki.count(a) > 1:
        for i in range(wyniki.count(a)-1):
            wyniki.remove(a)
print(wyniki)


