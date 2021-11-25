#Zadanie 7

def lista(list):
    print(' '.join([str(item) for item in list]).center(30))
    # kazdy item z listy połącz w ciąg dołączając ' ' pomiędzy nie i wycentruj zajmując 30 znaków

n = int(input("Podaj liczbe poziomow: "))
line = [1] #bo wierzchołek trójkąta to 1
lista(line)
for i in range(n - 1):
    next_line = [1] #bo krawędż trójkąta to 1
    for j in range(len(line) - 1):
        next_line.append(line[j] + line[j + 1]) 
        #dołącza kolejny wyraz do listy z własności trójkąta Pascala
    next_line.append(1) #bo krawędż trójkąta to 1
    line = next_line
    lista(line)
