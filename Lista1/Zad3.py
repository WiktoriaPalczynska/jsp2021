#Zadanie 3

import math
a=float(input())
b=float(input())
alfa=math.radians(float(input())) #funkcja radians() zwraca wartość przerobioną na radiany
Pole=(a*b*math.sin(alfa))/2 #wzór na pole trójkąta 
print(Pole)