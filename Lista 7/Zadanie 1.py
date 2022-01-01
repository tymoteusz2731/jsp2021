import time
from timeit import default_timer as timer
#rekurencja
def rekurencyjnie(n):
   if n <= 1:
       return n
   else:
       return(rekurencyjnie(n-1) + rekurencyjnie(n-2))

n = int(input("Wprowadź n: "))
tic = time.time()
for i in range(n):
    print(rekurencyjnie(i))
tac = time.time()

print("Czas renderowania: ", tac - tic)

#z pętlą for
tic = time.time()
start = timer()
a = 0
b = 1
wynik = 0
for i in range(0,n):
    if(i == 0):
        wynik = 0
    elif(i == 1):
        wynik = 1
    else:
        wynik = a + b
        a = b
        b = wynik
    print(wynik)
tac = time.time()
end = timer()
print(f"Czas renderowania: {tac - tic: .3E}")
print(f"Czas renderowania dokładniejszy: {end - start: .3E}")
