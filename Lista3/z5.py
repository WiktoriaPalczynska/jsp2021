#Zadanie 5 

import re #zaimportuj biblioteke obsługującą wyrazenia regularne

password=input("Podaj haslo: ")

#re.search() znajduje wzorzec w tekście
if (re.search(r"[a-z]",password)
    and re.search(r"[A-Z]",password)
    and re.search(r"[0-9]",password)
    and re.search(r"[$#@]",password)
    and 6<=len(password)<=16):
    print("Poprawne hasło")
else:
    print("Niepoprawne hasło!")



