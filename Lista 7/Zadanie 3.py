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


def SortowanieB(lista):
    tic = time.time()
    start = timer()
    n = len(lista)
    while n > 1:
        for l in range(0, n-1):
            if lista[l] > lista[l+1]:
                lista[l], lista[l+1] = lista[l+1], lista[l]
        n -= 1
    tac = time.time()
    stop = timer()
    print(tac - tic)
    print(stop - start)
    return lista

print(SortowanieB(losowe(100)))
print(SortowanieB(losowe(200)))
print(SortowanieB(losowe(300)))
