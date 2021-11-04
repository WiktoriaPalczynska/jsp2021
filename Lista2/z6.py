#Zadanie 6
lista=['Kasia','Basia','Marek','Darek']
lista.append('Józek') #dołącza 'Józek' na koniec listy (nawet liste jak jest pusta)
lista.extend(['Ania','Basia']) #dołącza na koniec elementy, które są w liście
lista.sort() #sortowanie elementów rosnąco
print(lista[3]) #wyswietla 4 element listy
print(lista[0:2]) #wyswietla 1 i 2 element listy
print(lista[-2::]) #wyswietla 2 ostatnie elementy listy
lista.remove('Basia') #usuwa zmienną 'Basia'
lista.remove('Basia') #wywoluje drugi raz, bo na liscie mamy więcej powtarzającyh się elementów
print(len(lista)) #wyświetla ilość studentów na liście
krotka=tuple(lista) #z ostatecznej listy tworze krotke
print(type(krotka))