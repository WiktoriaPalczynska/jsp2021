#Zadanie 3

import math

def na_stopnie(x):
    return math.degrees(x)

def na_radiany(x):
    return math.radians(x)

print("Konwertuj z: ")
print("a) radianów na stopnie")
print("b) stopni na radiany")

x=input()
if x=='a':
    a=int(input("Podaj radiany: "))
    print(na_stopnie(a))
elif x=='b':
    b=int(input("Podaj stopnie: "))
    print(na_radiany(b))
else:
    print("Nie ma takiej opcji do wybru!")