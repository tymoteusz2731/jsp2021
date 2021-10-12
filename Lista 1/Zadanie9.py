rz=float(input("Część rzeczywista: "))
ur=float(input("Część urojona: "))
zes=complex(rz,ur) # łączy dwie poprzednie liczby w liczbę zespoloną
print("Wartość bezwzględna: ",abs(zes))
print("Sprzężenie zespolone: ", zes.conjugate())