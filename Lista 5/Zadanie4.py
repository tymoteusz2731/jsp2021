def szyfruj(program, tekst):
    output = []
    if program == 0: #szyfrowanie
        kluczpomoc = ["a","e","i", "o", "y"]
        klucz={"a" : "y"  ,   "e" : "i"   ,   "i" : "o"   ,   "o" : "a"   ,   "y" : "e"}
        x = list(tekst)
        for i in x:
            if i in kluczpomoc:
                i = klucz[i]
                output.append(i)
            else:
                output.append(i)
        print(''.join(output))
    elif program == 1: #deszyfrowanie
        kluczpomoc = ["y","i","o", "a", "e"]
        klucz={"y" : "a"  ,   "i" : "e"   ,   "o" : "i"   ,   "a" : "o"   ,   "e" : "y"}
        x = list(tekst)
        for i in x:
            if i in kluczpomoc:
                i = klucz[i]
                output.append(i)
            else:
                output.append(i)
        print(''.join(output))
    else:
        print("Błędny program")



tekst = input("Wprowadź tekst: ")
program = int(input("Szyfrowanie = 0, Deszyfrowanie = 1: "))
szyfruj(program,tekst)