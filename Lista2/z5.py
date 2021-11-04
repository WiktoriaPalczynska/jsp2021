#Zadanie 5
napis=input()
dl=len(napis) #dlugosc zmiennej 'napis'
x=napis[0:(dl//2)]+'Python'+napis[(dl//2)::] #x to 2 pierwsze litery wczytanego napisu, "Python" i 2 ostatnie litery wczytanego napisu
print(x.strip()) #strip() usuwa spacje 
