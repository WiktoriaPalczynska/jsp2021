import os
import datetime

def data_uro(number):
    year = int(number[0:2])
    month = int(number[2:4])
    day = int(number[4:6])
    year += {
        0: 1900,
        1: 2000,
        2: 2100,
        3: 2200,
        4: 1800,
    }[month // 20]
    month = month % 20
    try:
        return datetime.date(year, month, day)
    except ValueError:
        raise InvalidComponent()

def plec(number):
    if number[11] in '02468':  # parzyste
        return 'K'
    else:  # nieparzyste
        return 'M'

def Pesel(string):
    for x in range (len(string)):
        print (x)


def sprawdz_sciezka():
    try: #próba otworzyć plik
        f = open("PESEL.TXT", "r")
        fileToString("PESEL.TXT")
        return 1
    except FileNotFoundError: 
        print("Plik nie znaleziono!") 
        sprawdz_sciezka()

def stworz_folder(value):
    f = open("PESELDESZYFR.txt","w+")
    f.write(value)
