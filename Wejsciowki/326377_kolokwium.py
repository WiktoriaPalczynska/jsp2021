lista_a=[1,2,4,5] #deklaruje liste
dl=len(lista_a) #długość listy
x=5
def licz_wielomian(x,lista_a): #funkcja pobiera dwa argumenty 
    suma=0
    for i in range(1,dl):
        wielomian=lista_a[i]*(x**i)
        suma+=wielomian
    suma1=lista_a[0]+suma #liczy wielomian
    print(suma1) #wypisuje wynik na ekranie
licz_wielomian(x,lista_a) #wywołanie funckji