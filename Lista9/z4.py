import matplotlib.pyplot as plt

nazwa = ["Pyython","C","Java","C++","C#","Visual Basic","Java Script","Assemly language","SQL","Swift"]
popularność  = [13.58,12.44,10.66,8.29,5.68,4.74,2.09,1.85,1.80,1.41]

plt.figure(figsize=(15, 5))

plt.bar(nazwa, popularność, color='green')
plt.suptitle("Wykres popularności języków programowania") #tytuł
plt.ylabel("Popularność w %") #oś y
plt.xlabel("Języki programowania") #oś x
plt.show() #pokaż wykres na ekranie