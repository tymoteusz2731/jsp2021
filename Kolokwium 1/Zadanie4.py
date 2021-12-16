import collections
liczba = float(input("Wprowadź liczbę zmiennoprzecinkową: "))
liczba = list(str(liczba))

czesccalkowita = []
czesculamkowa =[]
czyCalkowita = True

for i in range(len(liczba)):
    if(liczba[i]) == ".":
        czyCalkowita = False
    elif(czyCalkowita == True):
        czesccalkowita.append(liczba[i])
    else:
        czesculamkowa.append(liczba[i])

print("W części całkowitej: ", collections.Counter(czesccalkowita))
print("W części ułamkowej: ", collections.Counter(czesculamkowa))