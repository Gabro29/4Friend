import random
from math import factorial

count = 1
f = open("60000_parole_italiane.txt", "at")
words = ""

for i in open("60000_parole_italiane.txt"):
    words += i

frase_da_anagrammare = input(f"Inserisci una frase da anagrammare\n")


supp = []
match = []
s = 0
poss_anagramma = ""
repeat = []
dizi = []
pers_dizi = []

repeat.append(frase_da_anagrammare)

dizi = words.splitlines()

for i in range(0, len(frase_da_anagrammare)-2):
    for word in dizi:
        if frase_da_anagrammare[i] == word[0]:
            pers_dizi.append(word)

n = (len(frase_da_anagrammare))
durata = factorial(8)
k = 1

while k <= durata:
    a = random.randrange(n)
    k += 1
    if count == 1:
        supp.append(a)
        poss_anagramma += frase_da_anagrammare[a]
        count += 1
    elif a in supp and 1 < count < (n+1):
        pass
    elif count == n+1:
        if poss_anagramma in words.splitlines() and poss_anagramma not in repeat:
            print(f"{poss_anagramma}")
            repeat.append(poss_anagramma)
            poss_anagramma = ""
            supp.clear()
            count = 1
        else:
            repeat.append(poss_anagramma)
            poss_anagramma = ""
            supp.clear()
            count = 1
    else:
        supp.append(a)
        poss_anagramma += frase_da_anagrammare[a]
        count += 1
