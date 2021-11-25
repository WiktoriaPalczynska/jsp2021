#Zadanie 4

def n_element(n):
    a1=1 #pierwszy element ciągu
    q=2 #iloczyn ciągu geometrycznego
    return a1*(q**(n-1))

n=int(input("Podaj liczbe elementów ciągu: "))
print(n," element ciągu geometrycznego to: ",n_element(n))