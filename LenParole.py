
# Data una lista contenente parole restituisce in output una lista di interi che rappresentano la lunghezza delle parole

listA=[]
listB=[]

print(f"Inserisci le parole di cui vuoi sapere la lunghezza\n")
print(f"Digita terminato per non inserire più parole")

while True:

    parola=input(f"Inserisci parola ")

    if parola == "terminato":
        break
    else:
        listA.append(parola)

for oggetto in listA:

    listB.append(len(oggetto))

print(f"La lista di parole inserita è {listA}\nLa lunghezza delle rispettive parole è {listB}\n")
