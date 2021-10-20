zada=[]
a=range(3,100,3)
for n in a:
    zada.append(n)
print(zada)
#b
del zada[4:len(zada):3]
print(zada)
#c
suma=sum(zada)/len(zada)
print('Średnia to:', suma)