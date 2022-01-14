import itertools

class trojki(list):
    def __init__(self,lista):
        self.lista=lista
    def dzialaj(self):
        lista =[]
        for i in range(len(self.lista) + 1):
            zmienna = itertools.combinations(self.lista,i)
            lista += list(zmienna)
        for i in lista:
            if len(i) == 3 and sum(i) == 0:
                print(i)
    pass

lista = trojki([1,2,3,-3,0])
lista.dzialaj()


