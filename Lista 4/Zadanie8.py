def suma(n):
    wynik = 0.0
    for i in range(1,n+1):
        wynik = wynik + 1/i
    return wynik

print(suma(5))
