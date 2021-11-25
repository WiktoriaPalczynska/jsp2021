#Zadanie 10
def nwd(a,b):
    while b: 
        a,b=b,a%b
    return a

a = int(input("Podaj 1 liczbe: "))
b = int(input("Podaj 2 liczbe: "))
print("NWD podanych liczb to:", nwd(a,b))