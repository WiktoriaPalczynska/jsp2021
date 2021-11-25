#Zadanie 6
'''
Modul colorsys definiuje konwersje kodowania pomiędzy kolorami wyrażonymi w przestrzeni kolorów RGB,
a innymi ukladami wspolrzednych. W naszym przypadku drugi układ to HSV(wartosc nasycenia odcienia).
'''

import colorsys

r=float(input("Podaj R:"))
g=float(input("Podaj G:"))
b=float(input("Podaj B:"))

hsv=colorsys.rgb_to_hsv(r,g,b)
print("RGB:",(r,g,b))
print("HSV:", hsv)
