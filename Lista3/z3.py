#Zadanie 3
import math

a=int(input("Podaj a: "))
b=int(input("Podaj b: "))
c=int(input("Podaj c: "))

if a!=0:
    delta=b**2-4*a*c
    pierwiastek_delta=math.sqrt(delta)
    if delta>0:
        x1=(-b-pierwiastek_delta)/(2*a)
        x2=(-b+pierwiastek_delta)/(2*a)
        print("Pierwiastki rzeczywiste: ",x1,"i",x2)
    elif delta==0:
        x0=(-b)/2*a
        print("Pierwiastki rzeczywiste: ",x0)
    else:
        print("Sprzeczność! Brak pierwiastków rzeczywistych")
else:
    print("To nie równanie kwadratowe!")