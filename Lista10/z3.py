from itertools import combinations
from math import isclose


class Trzy:
    def __init__(self, tab):
        self.tab = tab

    def znajdz(self):
        if len(self.tab)>3:
            sublists = [list(item) for item in combinations(
                self.tab, 3) if isclose(sum(item), 0, abs_tol=0.0)]
            return "Ta lista nie posiada podlist spełniających warunek." if len(sublists) == 0 else sublists
        else:
            return "Lista jest zbyt krótka do wykonania tej metody."


lista = Trzy([-7, 16, -9, 3 ,2 ,-5, 9, 0, 1, 4])
print("Wszystkie potrójne podlisty, ktorych suma wynosi 0 to:")
print(lista.znajdz())

