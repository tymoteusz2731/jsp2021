import math
import matplotlib.pyplot as plt

v0 = float(input("Podaj prędkosc poczatkowa: "))
kat = float(input("Podaj kat rzutu: "))

v0y = v0 * math.sin(math.radians(kat))
v0x = v0 * math.cos(math.radians(kat))
Hmax = ((v0y)**2) / (2* 9.81) #wysokosc maksymalna

Z = (v0**2 / 9.81)*math.sin(math.radians(2*kat)) # zasięg
t = (2*v0 * math.sin(math.radians(kat)))/9.81 # czas lotu

tablicavx = []
tablicavy = []
i = 0

while i < t:
    vx = v0 * math.cos(math.radians(kat))
    tablicavx.append(vx)
    vy = v0 * math.sin(math.radians(kat)) - 9.81 * i
    tablicavy.append(vy)
    i += 0.05

tablicax=[]
tablicay=[]
i=0

while i < t:
    y = v0y * i * math.sin(math.radians(kat)) - 9.81/2 * i**2
    tablicay.append(y)
    x = v0x * i * math.cos(math.radians(kat))
    tablicax.append(x)
    i += 0.05

tablicat=[]
i=0
while i < t:
    tablicat.append(i)
    i += 0.05

fig,axs = plt.subplots(2)
axs[0].plot(tablicat,tablicavy)
axs[1].plot(tablicax,tablicay)