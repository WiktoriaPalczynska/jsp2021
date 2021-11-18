#Zadanie 10

lista=[]
for i in range(100,401):
    s = int((i/100)) #wylicza całkowite cyfry setek
    d = int(((i%100)/10)) #wylicza całkowite cyfry dziesiątek
    j = i%10 #wylicza całkowite cyfry jedności
    if s%2==0 and d%2==0 and j%2==0: #warunek na cyfre parzystą
        lista.append(i) #dołącza element do listy
print(lista)