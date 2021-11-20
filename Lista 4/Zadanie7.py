
def silnia(n):
    if n > 1:
        return n*silnia(n-1)
    return 1

n=10
for i in range(n):
    for j in range(n-i+1):
        print(' ',end='')
    for j in range(i+1):
        print(int(silnia(i)/(silnia(j)*silnia(i-j))), end=' ')
    print('\n')
