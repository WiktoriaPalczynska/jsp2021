import SzyfrCezara as cez
import os                   #obsługa ścieżek
from datetime import date

n = int(input("Podaj klucz szyfrowania w zakresie 1-10: "))
while n < 1 or n > 10: #zakres dla klucza(przesunięcia)
    print("Klucz nie mieści się w zakresie!")
    n = int(input("Podaj klucz szyfrowania w zakresie 1-10: "))

filepath = input("Podaj ścieżkę do pliku do zaszyfrowania: ")

def sprawdz_sciezka(filepath):
    try: #próba otworzyć plik
        f = open(filepath, "r", encoding="utf-8")
        return 1
    except FileNotFoundError: 
        print("Plik nie znaleziono!") 
        sprawdz_sciezka()


def stworz_katalog(zaszyfr):
    dzis = date.today()
    sciezka = input("Wprowadz sciezke do zapisania: ")
    try:
        os.makedirs(sciezka) #tworzy katalog
        os.chdir(sciezka) #zmień bieżący katalog roboczy na 'ścieżka'
        nazwa = 'plik_zaszyfrowany.txt{0}_{1}.txt'.format(n,dzis)
        f = open(nazwa,"w+")
        f.write(zaszyfr)
        return 1
    except IOError:
        print("Podana sciezka juz istnieje!")

def szyfr(sciezka):
    zapis = ""
    f = open(sciezka, "r")
    tekst = f.readlines() #wczytuje do zmiennej dane pliku
    for x in tekst:
        zapis += x
    zapis_plik=cez.szyfruj(zapis, n) #wywołanie funkcji z modułu
    stworz_katalog(zapis_plik) 

szyfr(filepath)



