#Zadanie 1

samogloska=['a','e','i','o','y','u'] #deklaracja tablicy z samogloskami
litera=input("Podaj litere: ")
if litera in samogloska: #in czy zmienna zawarta w innym obiekcie
    print('To samogloska')
else:
    print('To spolgloska')