napis=input("Wprowadź napis: ")
tablica=list(napis)
if (len(napis)%2 == 0):
    tablica.insert(len(napis)//2,'PYTHON')
    tablica=''.join(tablica)
    print(tablica)
else:
    tablica.pop(int(len(napis)/2+0.5)) #Bierze połowę i dodaje do tego 0,5 by osiągnąć liczbę naturalną + konwertuje na int
    tablica.insert(len(napis)//2,'PYTHON')
    tablica=''.join(tablica)
    print(tablica)