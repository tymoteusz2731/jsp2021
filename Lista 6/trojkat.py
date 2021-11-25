import math
def obwod(a,b,c):
    wynik = a + b + c
    return wynik
def pole(a,b,c):
    p = 0.5*(a+b+c)
    wynik = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return wynik
def rowno(a,b,c):
    if a==b and b==c and a==c:
        wynik = "Jest to trójkąt równoboczny"
    elif a==b or b==c or a==c:
        wynik = "Jest to trójkąt równoramienny"
    else:
        wynik = "Jest to trójkąt różnoboczny"
    return wynik
def prosty(a,b,c):
    if a**2+b**2 == c**2:
        wynik = "Jest to trójkąt prostokątny"
    if a**2+b**2 < c**2:
        wynik = "Jest to trójkąt rozwartokątny"
    else:
        wynik = "Jest to trójkąt ostrokątny"
    return wynik


