def ciag(n,a1=1,q=2):
    an=a1*(q**(n-1))
    return an

n = int(input("Wprowadź numer elementu ciągu: "))
a1 = int(input("Wprowadź wartość pierwszego elementu ciągu: "))
q = int(input("Wprowadź wartość iloczynu ciągu geometrycznego: "))
print(ciag(n,a1,q))