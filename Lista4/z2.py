#Zadanie 2

lista=[1,2,3,1,5,2,7,5,9]

def powtorzenia(x):
    return list(set(x)) #set() tworzy kolekcję uporządkowanych i unikalnych elementów.

print(lista)
print(powtorzenia(lista))