#Zadanie 3

def RomToDec(x):
    rzym = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    x = x.upper()
    
    dec = 0 
    i = 0
    while i < len(x):
        if i+1<len(x):
            if rzym[x[i]]<rzym[x[i+1]]:
                dec += rzym[x[i+1]] - rzym[x[i]]
                i += 2
            else:
                dec += rzym[x[i]]
                i += 1
        else:
            dec += rzym[x[i]]
            i += 1
    
    return dec

a=input("Wprowadź liczbę rzymską:")
print("Dziesiętnie: ",RomToDec(a))