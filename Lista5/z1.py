#Zadanie 1

slownik={'nic':'','jeden':1,'dwa':2,'trzy':3,'cztery':4,'pięć':5,'sześć':6,'siedem':7,'osiem':8,'dziewięć':9,
        'dziesięć':10,'jedenaście':11,'dwanaście':12,'trzynaście':13,'czternaście':14,'piętnaście':15,
        'szesnaśćie':16,'siedemnaście':17,'osiemnaście':18,'dziewiętnaście':19,'dwadzieścia':20,
        'trzydzieści':30,'czterdzieści':40,'pięćdziesiąć':50}

def zamiana(d,j):
    if j=='nic':
        if d in slownik:
            l=slownik.get(d) #uzyskaj wartość d
        return(l)
    else:
        if d in slownik:
            l=slownik.get(d) #uzyskaj wartość d
        if j in slownik:
            j=slownik.get(j) #uzyskaj wartość j
        return(l+j) #zwróć wartość wartości d i wartości j

x=input("Podaj słownie liczbę: ")
y=x.split() #tworzenie z łańcucha listy
y.append('nic') #dołącza puste miejsce 
print(zamiana(y[0],y[1])) #wyświetli 0 i 1 indeks listy

