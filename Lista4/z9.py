#Zadanie 9

def silnia(n):
    if n>1: return n*silnia(n-1) #obliczanie silni rekurencyjnie 
    elif n in (0,1): return 1
    
n = int(input("Podaj n: "))
print("Silnia n wynosi:",silnia(n))