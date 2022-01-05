import time
import random

def wypisz(tab): #tworzymy metode do wypiswania zawartosci naszej tablicy
    for el in tab:
        print(el, end=" | ")
def sortuj_wstaw(tab, n): #tworzymy metode do sortowania poprzez wstawianie
    for x in range(1, n):
        selected = tab[x]  #aktualnie wybrany element
        y = x-1 #przygotowujemy iteracje poprzez pozostale elementy
        while y >= 0 and selected < tab[y]: #dopoki nie znajdziemy elementu mniejszego od wybranego i nie natrafimy na poczatek tablicy
            tab[y+1] = tab[y] #zamieniamy elementy miejscami
            y -= 1 #modyfikujemy zmienna iteracyjna
        #print("\nKrok ", (x-1), ": przenoszenie elementu  ", selected, " z pozycji ", x, " na pozycje ", (y+1))
        tab[y+1] = selected #po znalezieniu mniejszego elementu, zamieniamy go z wybranym
        #wypisz(tab)


lista1 = []  # pusta lista
for i in range(0, 101):
    lista1.append(random.randint(0, 20))

lista2 = []  # pusta lista
for i in range(0, 201):
    lista2.append(random.randint(0, 20))

lista3 = []  # pusta lista
for i in range(0, 301):
    lista3.append(random.randint(0, 20))

#print("Lista 1: ",lista1)
start1 = time.time()
#print("Lista 1 (po posortowaniu):")
#print(sortuj_wstaw(lista1,101))
sortuj_wstaw(lista1,101)
end1 = time.time()
total1 = end1 - start1
print("Czas wykonanania 1 listy: ", "{0:08f}s".format(total1))

#print("\nLista 2: ",lista2)
start2 = time.time()
#print("Lista 2 (po posortowaniu):")
#print(sortuj_wstaw(lista2,201))
sortuj_wstaw(lista2,201)
end2 = time.time()
total2 = end2 - start2
print("Czas wykonanania 2 listy: ", "{0:08f}s".format(total2))

#print("\nLista 3: ",lista3)
start3 = time.time()
#print("Lista 3 (po posortowaniu):")
#print(sortuj_wstaw(lista3,301))
sortuj_wstaw(lista3,301)
end3 = time.time()
total3 = end3 - start3
print("Czas wykonanania 3 listy: ", "{0:08f}s".format(total3))