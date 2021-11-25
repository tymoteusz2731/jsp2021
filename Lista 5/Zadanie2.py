tekst = 994
wynik = []
mnoznik = 1
jednosci = {
    "zero": 0, "jeden": 1, "dwa": 2, "trzy": 3, "cztery": 4, "pięć": 5, "sześć": 6, "siedem": 7, "osiem": 8, "dziewięć": 9, "dziesięć": 10, "jedenaście": 11, 
    "dwanaście": '12', "trzynaście": 13, "czternaście": 14, "piętnaście": 15, "szesnaście": 16, "siedemnaście": 17, "osiemnaście":18, "dziewiętnaście": 19, 
    "dwadzieścia": 20, "trzydzieści": 30, "czterdzieści": 40, "pięćdziesiąt": 50, "sześćdziesiąt": 60, "siedemdziesiąt": 70, "osiemdziesiąt": 80, "dziewięćdziesiąt": 90,
    "sto":100,"dwieście":200,"trzysta":300,"czterysta":400,"pięćset":500,"sześćset":600,"siedemset":700,"osiemset":800,"dziewięćset":900,"tysiąc":1000}

x = [int(d) for d in str(tekst)]

jednosci_odtylu = {slownie: liczba for liczba, slownie in jednosci.items()} #zamiana kolejności w słowniku
print(jednosci_odtylu)

for i in range(len(x)-1,-1,-1): #zaczyna od jedności i idzie w górę
    robocza = x[i] #przypisanie do lokalnej zmiennej
    robocza = robocza * mnoznik # pomnożenie przez mnożnik zależny od tego czy to jedność czy np. setka
    robocza = jednosci_odtylu[robocza] # zamiana wartości na wartość z odwróconego słownika
    wynik.insert(0,robocza) # wrzucenie wyniku to tablicy, ale na jej początek
    mnoznik = mnoznik * 10 # zwiększenie mnożnika czyli jednostek na dziesiątki itp.
print(' '.join(wynik)) # konwersja tablicy na tekst