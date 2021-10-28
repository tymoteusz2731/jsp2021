lista=range(99,401)
listaa=list(lista)
wynik=[]
for i in lista:
    if i%2==0:
        wynik.append(i)
print(wynik, sep=',')

