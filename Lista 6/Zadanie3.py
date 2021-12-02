def patrzimow(i):
    if i == 1:
        return "1"
    if i == 2:
        return "11"
    zmienna = '11'
    for a in range(3,i+1):
        ile_powtorzen = 1
        zmiennap = ''   
        for b in range(1,len(zmienna)):   
            if zmienna[b] != zmienna[b-1]:
                zmiennap = zmiennap + str(ile_powtorzen)
                zmiennap = zmiennap + zmienna[b-1]
                ile_powtorzen = 1
            else:
                ile_powtorzen = ile_powtorzen + 1
       zmienna = zmiennap
    return zmienna
print(patrzimow(5))
