#Zadanie 10

import cmath
z=complex(0,1)

print("Część rzeczywista dla sin(z): ", cmath.sin(z).real ) #real część rzeczywista
print("Część zespolona dla sin(z): ", cmath.sin(z).imag) #imag częśc urojona
print("Część rzeczywista dla cos(z): ", cmath.cos(z).real)
print("Część zespolona dla cos(z): ", cmath.cos(z).imag)

print((cmath.sin(z))**2+(cmath.cos(z))**2==1, "poniewaz to",(cmath.sin(z))**2+(cmath.cos(z))**2)