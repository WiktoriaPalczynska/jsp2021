class Sublist:
    def __init__(self, array):
        self.array = array

    def podlista(self): #metoda zwracająca wszystkie "podlisty" podanej listy.
        podlista = [[]]

        for i in range(len(self.array) + 1):
            for j in range (i + 1, len(self.array) + 1):
                sub = self.array[i:j]
                podlista.append(sub)
        return podlista

def main():
    sublist = Sublist([1, 2, 3])
    print(sublist.podlista())


if __name__ == "__main__":
    main()