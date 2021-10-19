listastudentow=['Kasia','Basia','Marek','Darek']
listastudentow.append('Józek')
listastudentow.extend(['Ania','Basia'])
listastudentow.sort()

print(listastudentow[3])
print(listastudentow[0:2])
print(listastudentow[-3:-1], sep=', ')
while (listastudentow.count('Basia')): #zwraca liczbę wystąpień "basia"
    listastudentow.remove('Basia')
print(listastudentow)
print(len(listastudentow))
print(tuple(listastudentow))