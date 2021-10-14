#Zadanie 9

import cmath
import math
r=float(input("Podaj część rzeczywistą: "))
i=float(input("Podaj część urojoną: "))
z=complex(r,i)
arg=math.cos(r/abs(z)) #fi to argument liczby zespolonej, gdy mamy np. sin fi = 1/2 to arg=pi/6
print("Moduł wynosi: ", abs(z)) #abs(z) to moduł liczby zespolonej; moduł=(a**2 + b**2)**(1/2)
print("Argument wynosi: ", arg)
print("Sprzężenie wynosi: ", z.conjugate())