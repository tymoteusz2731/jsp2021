#zadanie 3
import math
a=float(input("Podaj a: "))
b=float(input("Podaj b: "))
alfa=float(input("Podaj kąt między bokami: "))
alfa=math.radians(alfa)
print(a*b*math.sin(alfa))
