def szyfrowanie(tekst,przesuniecie):
    lista_odrzuconych = [' ',1,2,3,4,5,6,7,8,9,0,'','@','#','%','^','&','*','(',')']
    tekst = list(tekst)


    for i in range(len(tekst)):
        if tekst[i] not in lista_odrzuconych:
            tekst[i] = ord(tekst[i])
            tekst[i] += przesuniecie
            tekst[i] = chr(tekst[i])
    tekst = ''.join(map(str,tekst))
    return tekst

def deszyfrowanie(tekst,przesuniecie):
    lista_odrzuconych = [' ',1,2,3,4,5,6,7,8,9,0,'','@','#','%','^','&','*','(',')']
    tekst = list(tekst)

    for i in range(len(tekst)):
        if tekst[i] not in lista_odrzuconych:
            tekst[i] = ord(tekst[i])
            tekst[i] -= przesuniecie
            tekst[i] = chr(tekst[i])
    tekst = ''.join(map(str,tekst))
    return tekst
