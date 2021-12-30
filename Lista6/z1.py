import trojkat

a = float(input("Podaj bok a: "))
b = float(input("Podaj bok b: "))
c = float(input("Podaj bok c: "))

boki = []
boki.extend([a,b,c])
sorted(boki)
if boki[0] + boki[1] > boki[2]:
    trojkat.obwod(a,b,c)
    trojkat.pole(a,b,c)
    trojkat.jaki_boczny(a,b,c)
    trojkat.jaki_katny(a,b,c)
else:
    print("Taki trójkąt nie istnieje.")


