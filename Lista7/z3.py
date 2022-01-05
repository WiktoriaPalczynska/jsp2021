import time
import random

def sortowanie_babelkowe(lista):
    n = len(lista)
    
    while n > 1:
        zamien = False
        for l in range(0, n-1):
            if lista[l] > lista[l+1]:
                lista[l], lista[l+1] = lista[l+1], lista[l]
                zamien = True
                
        n -= 1
        if zamien == False: break
        
    return lista


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
#print(sortowanie_babelkowe(lista1))
sortowanie_babelkowe(lista1)
end1 = time.time()
total1 = end1 - start1
print("Czas wykonanania 1 listy: ", "{0:08f}s".format(total1))

#print("\nLista 2: ",lista2)
start2 = time.time()
#print("Lista 2 (po posortowaniu):")
#print(sortowanie_babelkowe(lista2))
sortowanie_babelkowe(lista2)
end2 = time.time()
total2 = end2 - start2
print("Czas wykonanania 2 listy: ", "{0:08f}s".format(total2))

#print("\nLista 3: ",lista3)
start3 = time.time()
#print("Lista 3 (po posortowaniu):")
#print(sortowanie_babelkowe(lista3))
sortowanie_babelkowe(lista3)
end3 = time.time()
total3 = end3 - start3
print("Czas wykonanania 3 listy: ", "{0:08f}s".format(total3))