#Zadanie 7

def Fib(x):
    a=0 #wyraz 0 ciągu
    b=1 #wyraz 1 ciągu
    for i in range(1,x+1): #iteruj od  do argumentu+1
        b+=a #do b dodajemy a co iteracje
        a=b-a #przypisujemy do a wartość b-a co iteracje
        print(b) #wypisujemy b (kolejny wyraz ciągu)

N=int(input("Podaj ile wyrazów ciągu Fibonacciego: ")) 
Fib(N) #wywołanie funkcji

