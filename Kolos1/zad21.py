tablica=[]
dzwignia = True

while dzwignia == True:
    a = input("Wprowadź liczbę, zakończ wpisując 'end': ")
    if a == 'end':
        dzwignia = False
    else:
        tablica.append(a)

dzwignia = True
zmienna = 0

for i in tablica:
    if i.isnumeric() == True:
        zmienna += 1


minimum = min(tablica)
maximum = max(tablica)

if(zmienna == 0):
    print("Nie ma wartości numerycznych")
elif(minimum == maximum):
    print("Wartość minimalna i maksymalna są takie same")
else:
    print(tablica.index(minimum))
    print(tablica.index(maximum))
    
