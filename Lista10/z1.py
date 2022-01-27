import numpy as np

class Kolo:
    def __init__(self,r):
        self.r=r

    def obwod(self):
        return 2*np.pi*self.r
        
    def pole(self):
        return np.pi*self.r**2

r=int(input("Podaj promien: "))
kolo=Kolo(r)
print(f"Obwód: {kolo.obwod()}")
print(f"Pole: {kolo.pole()}")
