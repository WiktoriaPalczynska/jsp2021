#Zadanie 9

m=int(input("Podaj ilosc wierszy: "))
n=int(input("Podaj ilosc kolumn: "))

for y in range(1,m+1):
    for x in range(1,n+1):
        print(f"{x*y:^4}",end="|") #formatowanie
    print()





