#Zadanie 1

lista=[1,2,3,4,5]
print("Suma elementów listy wynosi: ",sum(lista))

def mnozenie(l):
    iloczyn=1
    for i in range(0,len(l)):
        iloczyn*=l[i]
    print("Iloczyn elementów listy wynosi: ",iloczyn)

mnozenie(lista)
