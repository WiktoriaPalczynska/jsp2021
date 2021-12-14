#Zadanie 4

def szyfrowanie(n):
	klucz = {'a' : 'y', 'e' : 'i', 'i' : 'o', 'o' : 'a', 'y' : 'e'}
	szyfr = ''.join([klucz.get(k,k) for k in n])
	return szyfr
	
def odszyfrowanie(szyfr):
	klucz = {'a' : 'y', 'e' : 'i', 'i' : 'o', 'o' : 'a', 'y' : 'e'}
	deszyfr = []
	for s in list(szyfr):
		k = klucz.get(s,s)
		if k == s:
			deszyfr.append(s)
		else:
			for i,v in klucz.items():
				if s == v:
					deszyfr.append(i)
	deszyfr = ''.join(deszyfr)
	return deszyfr

text=input("Podaj tekst: ")
x=szyfrowanie(text)
print("Zaszyfruj: ",x)
print("Odszyfruj: ",odszyfrowanie(x))