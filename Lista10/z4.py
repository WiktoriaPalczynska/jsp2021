import xml.etree.ElementTree as ET

class Kursy:
    def __init__(self, filepath):
        self.path = filepath
        self.tree = ET.parse(filepath)
        self.root = self.tree.getroot()

    def lista_kursow(self):
        index = 1
        for nazwa_waluty, przelicznik, kod_waluty, kurs_sredni in self.root.iter('pozycja'):
            print(f"{index}. {nazwa_waluty.text} ({kod_waluty.text})")
            index += 1

    def pln_to_wal(self, wal, ile):
        for nazwa_waluty, przelicznik, kod_waluty, kurs_sredni in self.root.iter('pozycja'):
            if wal == kod_waluty.text:
                kurs = kurs_sredni.text
                kurs = kurs.replace(",",".")
                return f"{ile * float(przelicznik.text) / float(kurs)} {kod_waluty.text}"

    def wal_to_pln(self, wal, ile):
        for nazwa_waluty, przelicznik, kod_waluty, kurs_sredni in self.root.iter('pozycja'):
            if wal == kod_waluty.text:
                kurs = kurs_sredni.text
                kurs = kurs.replace(",",".")
                return f"{ile * float(przelicznik.text) * float(kurs)} {'PLN'}"

    def wal_to_wal(self, wal, wal2, ile):
        temp = 0
        for nazwa_waluty, przelicznik, kod_waluty, kurs_sredni in self.root.iter('pozycja'):
            if wal == kod_waluty.text:
                kurs = kurs_sredni.text
                kurs = kurs.replace(",",".")
                temp = ile * float(przelicznik.text) * float(kurs)
        for nazwa_waluty, przelicznik, kod_waluty, kurs_sredni in self.root.iter('pozycja'):
            if wal2 == kod_waluty.text:
                kurs = kurs_sredni.text
                kurs = kurs.replace(",",".")
                return f"{temp * float(przelicznik.text) / float(kurs)} {kod_waluty.text}"


def switch(option):
    if option == 1:
        przel = Kursy("kursy.xml")
        print(przel.lista_kursow())
    elif option == 2:
        wal = input("Podaj kod wybranej waluty: ")
        ile = float(input("Podaj ile PLN chcesz wymienić: "))
        przel = Kursy("kursy.xml")
        print(przel.pln_to_wal(wal, ile))
    elif option == 3:
        wal = input("Podaj kod wybranej waluty: ")
        ile = float(input("Podaj ile chcesz wymienić: "))
        przel = Kursy("kursy.xml")
        print(przel.wal_to_pln(wal, ile))
    elif option == 4:
        wal = input("Podaj kod waluty, którą chcesz wymienić: ")
        wal2 = input("Podaj kod waluty, którą chcesz otrzymać: ")
        ile = float(input("Podaj ile chcesz wymienić: "))
        przel = Kursy("kursy.xml")
        print(przel.wal_to_wal(wal, wal2, ile))
    else:
        print("Wybierz poprawną opcję!")
        option = int(input(
        "Wybierz opcje: \n1 - lista kursow \n2 - konwersja PLN na wybrana walute \n3 - konwersja wybranej waluty na PLN \n4 - konwersja wybranej waluty na inna wybrana walute\n"))
        switch(option)


working = True
while working == True:
    option = int(input(
        "Wybierz opcje: \n1 - lista kursow \n2 - konwersja PLN na wybrana walute \n3 - konwersja wybranej waluty na PLN \n4 - konwersja wybranej waluty na inna wybrana walute\n"))
    switch(option)
    working = int(input("Czy kontynuować działanie programu?\n1 - TAK\n0 - NIE\n"))