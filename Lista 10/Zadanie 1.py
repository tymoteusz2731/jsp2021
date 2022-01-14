import math
class kolo:
    def __init__(self, r):
        self.r = r
    def pole(self):
        print("Pole to: ", math.pi * (self.r)**2)
    def obwod(self):
        print("Obwód to: ", 2 * math.pi * self.r)
    pass


kolko = kolo(10)
kolko.pole()
kolko.obwod()


