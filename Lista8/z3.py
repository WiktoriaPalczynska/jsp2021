import random    #obsługa liczb pseudolosowych
import os        #obsługa ścieżek

def pesel():

    pierwsza=random.randint(0,9)
    druga=random.randint(0,9)
    
    rok = random.randint(1900,2022)
    msc = random.randint (1,12)

    if rok <= 1999:
        kod=0 #kod stulecia
        if(msc>=10):
            trzy_cztery=msc
        else:
            trzy_cztery='0'+str(msc)

    elif rok >= 2000:
        kod=20
        trzy_cztery=msc+kod

    dzien_uro=random.randint(1,31) #dzien urodzenia
    if (dzien_uro >= 10):
        piec_szesc=dzien_uro
    else:
        piec_szesc='0'+str(dzien_uro)

    nieparzyste_months = (1, 3, 5, 7, 8, 10, 12)
    parzyste_months = (4, 6, 9, 11)

    if msc in nieparzyste_months:
        dzien = random.randint(1,31)

    elif msc in parzyste_months:
        dzien = random.randint(1,30)		

    else: #luty
        if rok % 4 == 0 and rok != 1900:
            dzien = random.randint(1,29) #rok przestępny

        else:
            dzien = random.randint(1,28) #rok nieprzestępny



    siedem_do_dziesiec = random.randint(1000,9999) #numer porządkowy
    #siedem_do_dziesiec = str(siedem_do_dziesiec)

    jedenasta=random.randint(0,9)

    return (str(pierwsza)+str(druga)+str(trzy_cztery)+str(piec_szesc)+str(siedem_do_dziesiec)+str(jedenasta))



f = open("PESEL.txt","w+")

for i in range (10):
    x = pesel()
    f.write(str(x) + '\n')