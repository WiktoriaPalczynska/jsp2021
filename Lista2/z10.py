#Zadanie 10

T=[] #definiuje tablice
for i in range(3,100,3): #iteruje od 3 do 100 co 3
    T.append(i) #dołącza element do listy T
print(T)
del T[4::3] #usuwa co trzeci element zaczynajac od 5
print(T)
sr=sum(T)/len(T) #liczy średnią arytmetyczną otrzymanej listy
print(sr)