#Zadanie 5

lista=[1,2,3,4,5,4,4,4]
x=len(lista)

def permutacje(x):
    f=lambda a:a*f(a-1) if a!=0 else 1
    return f(x)

print("Wszystkie permutacje listy wynoszą: ",permutacje(x)) 