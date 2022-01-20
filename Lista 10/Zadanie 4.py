import xml.etree.ElementTree as ET

class Waluty():
    def __init__(self, sciezka):
        root = ET.parse(sciezka).getroot()

        self.a = {}
        for pozycja in root.findall('pozycja'): # w pliku tym każdy element zaczyna się od tagu "pozycja":
            aprim = {} 
            nazwa = pozycja.find('nazwa_waluty').text
            przelicznik = pozycja.find("przelicznik").text
            kod = pozycja.find("kod_waluty").text
            kurs_sredni = pozycja.find("kurs_sredni").text
            kurs_sredni = kurs_sredni.replace(',','.')

            aprim['nazwa'] = nazwa
            aprim['przelicznik'] = int(przelicznik)
            aprim['kurs_sredni'] = float(kurs_sredni)

            self.a[kod] = aprim # dzięki temu mamy id : dane

    def kursy(self):
        for i in self.a:
            print(i, self.a[i])
    def nawalute(self, kod, ile):
        if kod not in self.a:
            print("Nie ma takiego kodu w bazie")
        else:
            przelicznik = self.a[kod]['przelicznik']
            kurs = self.a[kod]['kurs_sredni']
            wynik = przelicznik * (ile / kurs)
            return wynik
    def kazda(self,koda,kodb,ile):
        if koda not in self.a or kodb not in self.a:
            print("Nie ma takiego kodu w bazie")
        else:
            przelicznikaa = self.a[koda]['przelicznik']
            kursa = self.a[koda]['kurs_sredni']

            krokposredni = (ile / przelicznikaa) * kursa
            krokposredni = self.nawalute(kodb,krokposredni)

            return krokposredni






waluty = Waluty('plik.xml')
#waluty.kursy()

print(waluty.nawalute('EUR', 100))
print(waluty.kazda('EUR', 'USD', 100))