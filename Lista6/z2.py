import SzyfrCezara

wybierz=int(input("Wybierz:\n 1)szyfrowanie,\n 2)deszyfrowanie: \n"))
tekst=input("Podaj tekst: ")
klucz=int(input("Podaj klucz: "))
if(wybierz==1):
    SzyfrCezara.szyfruj(tekst,klucz)
if(wybierz==2):
    SzyfrCezara.deszyfruj(tekst,klucz)