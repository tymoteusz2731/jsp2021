m=int(input("Podaj m: ")) #wiersze
n=int(input("Podaj n: ")) #kolumny

for i in range(1,m+1):
    for j in range(1,n+1):
        print(i,"*",j,'=',i*j, end='    ')
    print('')
