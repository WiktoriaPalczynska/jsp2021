#Dla zadanego n generuje n pierwszych wyrazów ci¡gu "look-and-say".
#n-ty wyraz jest generowany przez odczytanie (n-1)-tego wyrazu.

def look_and_say(n):
    if (n == 1):
        return "1"
    if (n == 2):
        return "11"

    s = "11"
    for i in range(3, n + 1):
        s += '$'
        l = len(s)
 
        cnt = 1 
        tmp = ""

        for j in range(1 , l):
            if (s[j] != s[j - 1]):
                tmp += str(cnt + 0)
                tmp += s[j - 1]
                cnt = 1

            else:
                cnt += 1
 
        s = tmp
    return s
 
N = int(input("Podaj n: "))
print(look_and_say(N))
