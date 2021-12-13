slowo = input("Wprowadź słowo/zdanie: ")

slowo = slowo.replace(" ","")
zmienna = False
for i in range(len(slowo)):
    if slowo[i] != slowo[-1-i]:
        zmienna = True

if (zmienna == True):
    print("To nie jest palindrom")
else:
    print("To jest palindrom")