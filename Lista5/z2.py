#Zadanie 2

slownik={'0':'','1':'jeden','2':'dwa','3':'trzy','4':'cztery','5':'pięć','6':'sześć','7':'siedem','8':'osiem','9':'dziewięć',
        '00':'','10':'dziesięć','11':'jedenaście','12':'dwanaście','13':'trzynaście','14':'czternaście','15':'piętnaście',
        '16':'szesnaśćie','17':'siedemnaście','18':'osiemnaście','19':'dziewiętnaście','20':'dwadzieścia',
        '30':'trzydzieści','40':'czterdzieści','50':'pięćdziesiąć','60':'sześćdziesiąt','70':'siedemdziesiąt',
        '80':'osiemdziesiąt','90':'dziewięćdziesiąt','000':'','100':'sto','200':'dwieście','300':'trzysta','400':'czterysta',
        '500':'pięćset','600':'sześćset','700':'siedemset','800':'osiemset','900':'dziewięćset','1000':'tysiąc'}

def slownie(x):
        dl=len(x)
        if dl==4:
                t=x[0]+"000"
                tys=slownik.get(t)
                s=x[1]+"00"
                set=slownik.get(s)
                d=x[2]+"0"
                dz=slownik.get(d)
                print("Słownie: ",tys," ",set," ",dz," ",slownik.get(x[3]))
        elif dl==3:
                s=x[0]+"00"
                set=slownik.get(s)
                d=x[1]+"0"
                dz=slownik.get(d)
                print("Słownie: ",set," ",dz," ",slownik.get(x[2]))
        elif dl==2:
                d=x[0]+"0"
                dz=slownik.get(d)
                print("Słownie: ",dz," ",slownik.get(x[1]))
        elif dl==1:
                j=x[0]
                print("Słownie: ",slownik.get(j))
        
x=input("Podaj liczbę całkowitą od 1 do 1999: ")
slownie(x)
