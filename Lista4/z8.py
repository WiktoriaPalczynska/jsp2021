#Zadanie 8

def suma_elementow(n):
    suma=0.0
    for i in range(1,n+1):
        suma+=1.0/i
    return suma

n = int(input("Podaj n elementów ciągu harmonicznego: "))
print("Suma elementów szeregu harmonicznego wynosi:",suma_elementow(n))