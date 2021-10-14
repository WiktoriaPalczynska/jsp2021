#Zadanie 8

a=int(input("Podaj mniejszą liczbe: "))
b=int(input("Podaj większą liczbe: "))
Z=b%a
Z*=Z+3 #Z=Z*(Z+3) można skrócić do tej postaci
print(Z)