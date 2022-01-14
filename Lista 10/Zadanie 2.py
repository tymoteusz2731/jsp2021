import itertools

class podlista(list):
    def __init__(self,lista):
        self.lista=lista
    def dzialaj(self):
        lista =[]
        for i in range(len(self.lista) + 1):
            zmienna = itertools.combinations(self.lista,i)
            lista += list(zmienna)
        print(lista)
    def pokaz(self):
        print(self.lista)
    pass


lista = podlista([1,2,3])
lista.pokaz()
lista.dzialaj()







