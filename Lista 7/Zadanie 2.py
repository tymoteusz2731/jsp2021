import time
import random
from timeit import default_timer as timer
def losowe(N):
    lista = []
    i=0
    while i <= N:
        lista.append(random.randint(0,20))
        i += 1
    return lista

def Sortowanieb(A):
    tic = time.time()
    start = timer()
    for i in range(1,len(A)):
        klucz = A[i] #aktualny
        j = i - 1  #poprzedni
        while j>=0 and A[j]>klucz:  #poprzedni jest większy od aktualnego
            A[j + 1] = A[j]     #kolejnemu jest przypisywana wartość aktualnego
            j = j - 1 #zmiejszenie j celem cofania się by sprawdzić czy ta liczba nie jest mniejsza od jakiejś która już wystąpiła
        A[j + 1] = klucz
    tac = time.time()
    stop = timer()
    print(tac - tic)
    print(stop - start)
    return A


print(Sortowanieb(losowe(100)))
print(Sortowanieb(losowe(200)))
print(Sortowanieb(losowe(300)))