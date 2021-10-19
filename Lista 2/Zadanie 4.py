napis=input("Wprowadź napis: ")
rnap=list(napis)
pierwszy=rnap[0]
for i in range(1,len(rnap)):
    if rnap[i]==pierwszy:
        rnap[i]='$'
rnap=''.join(rnap)
print('Oto wynik: ',rnap)