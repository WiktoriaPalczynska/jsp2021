
def obwod(a,b,c):
    print("Obwód trójkąta: ",a+b+c)

def pole(a,b,c):
    p=(a+b+c)/2 #połowa obwodu
    print("Pole trójkąta: ",(p*(p-a)*(p-b)*(p-c))**0.5) #wzór Herona

def jaki_boczny(a,b,c):
    p=(a+b+c)/2
    P=(p*(p-a)*(p-b)*(p-c))**0.5
    if a==b==c:
        if P/(a*b/2)==(3**0.5)/2:
            print("To trójkąt równoboczny")
        else: print("To trójkąt równoramienny")
    else:
        print("To jest trójkąt różnoboczny")

def jaki_katny(a,b,c):
    if a**2+b**2==c**2:
            print("To trójkąt prostokątny")
    elif a**2+b**2<c**2:
            print("To trójkąt ostrokątny")
    elif a**2+b**2>c**2:
            print("To trójkąt rozwartokątny")
