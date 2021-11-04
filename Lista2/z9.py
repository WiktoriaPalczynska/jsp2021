#Zadanie 9

#chain.from_iterable wypłaszcza zbiór
from itertools import chain

lista=[[2,4,3],[1,5,6],[9],[7,9,0]]
x=chain.from_iterable(lista)
print(list(x)) #list() zwraca liste 
