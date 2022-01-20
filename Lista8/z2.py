import SzyfrCezara as cez
import os                   #obsługa ścieżek
from datetime import date
import re                   #operacje na wyrażeniach regularnych

filepath = input("Wprowadz sciezke: ")
s = filepath
result = re.search('txt(.*)_', s) #wyszukaj ciąg, któy kończy na „txt”
n = result.group(1) #zwraca część ciągu, w której było dopasowanie

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
        nazwa = 'plik_deszyfrowany.txt{0}_{1}.txt'.format(n,dzis)
        f = open(nazwa,"w+")
        f.write(zaszyfr)
        return 1
    except IOError:
        print("Podana sciezka juz istnieje!")

def deszyfr(sciezka):
    zapis = ""
    f = open(sciezka, "r")
    tekst = f.readlines() #wczytuje do zmiennej dane pliku
    for x in tekst:
        zapis += x
    zapis_plik=cez.deszyfruj(zapis, int(n)) #wywołanie funkcji z modułu
    stworz_katalog(zapis_plik) 

deszyfr(filepath)

