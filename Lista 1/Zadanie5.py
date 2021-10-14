#zadanie 5
import math
print(65.55124//2) #Funkcja "bierze" pełne części z dzielenia, nawet jeżeli reszta byłaby bliska pełnej całości, nie bierze tego pod uwagę. Nie ma możliwości dostosowania dokładności przybliżenia, o czym więcej w dalszych przykładach.
print(round(65.55124/2,2)) #Funkcja matematycznie zaokrągla liczbę, Dodatkowo możemy podać z jaką dokładnością chcemy przybliżyć (np. do 2 lub 3 miejsca po przecinku), wtedy stosujemy round(65.55124/2,2)
print(math.floor(65.55124/2)) #Funkcja działa podobnie do dzielenia bez reszty, w tym wypadku zwraca wynik w formacie "int"

