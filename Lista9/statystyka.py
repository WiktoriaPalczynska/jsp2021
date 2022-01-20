import sys #żeby mieć dostęp do wiersza poleceń
import numpy as np

def read_file(fn):
    with open(fn) as f: #with automatycznie zamyka plik
        return [float(x) for x in f]


fn,opt=sys.argv[1:]
data=read_file(fn)

if opt == "--srednia":
    print(np.mean(data))

elif opt == "--mediana":
    print(np.var(data))

elif opt == "--odchylenie":
    print(np.std(data))

else:
    print(f"{opt} is not in option")


