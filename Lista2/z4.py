#Zadanie 4
napis=input()
napis1=napis.replace(napis[0],'$') #napis1 to zmienna 'napis' z podmienionymi literami takimi jak jego pierwszy znak
napis2=napis[0]+napis1[1::] #napis2 to sklejenie piewszej litery zmiennej 'napis' i reszty liter za wyjątkiem 1 od 'napis1'
print(napis2)